import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  File? _image;
  String _resultText = "Sonuç bekleniyor...";
  final ImagePicker _picker = ImagePicker();

  // Eğer emülatörde çalışıyorsanız, '10.0.2.2' kullanın
  // Gerçek cihazda çalışıyorsanız, bilgisayarınızın yerel IP adresini kullanın
  String apiUrl = "http://XXX.XXX.XX.X:YYYY/predict"; // Bilgisayarınızın IP adresi ve Flask sunucu portu

  bool _isLoading = false; // Yükleniyor durumu

  // Fotoğraf seçimi için galeri açma
  Future<void> _pickImage() async {
    final pickedFile = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
        _resultText = "Fotoğraf seçildi, şimdi API'ye gönderin.";
      } else {
        _resultText = "Fotoğraf seçilmedi.";
      }
    });
  }

  // Fotoğrafı API'ye gönderme
  Future<void> _sendImageToApi() async {
    if (_image == null) {
      setState(() {
        _resultText = "Lütfen önce bir fotoğraf seçin.";
      });
      return;
    }

    setState(() {
      _isLoading = true; // Yükleniyor durumunu başlat
      _resultText = "Sonuç bekleniyor...";
    });

    try {
      var request = http.MultipartRequest(
        'POST',
        Uri.parse(apiUrl),
      );

      // Fotoğraf dosyasını ekle
      request.files.add(
        await http.MultipartFile.fromPath('image', _image!.path), // Flask 'image' parametresi
      );

      // API'ya isteği gönder ve yanıtı al
      var response = await request.send();
      print("Status Code: ${response.statusCode}");

      if (response.statusCode == 200) {
        var responseData = await http.Response.fromStream(response);
        var result = json.decode(responseData.body);

        // API yanıtını yazdır
        print("Response Body: ${responseData.body}");

        // Tahmin sonucunu ekrana yazdır
        setState(() {
          _resultText = result['result'] == "hasarlı"
              ? "Fotoğrafta hasar var."
              : "Fotoğrafta hasar yok.";
        });
      } else {
        // Başarısız olursa hata kodunu ekrana yazdır
        setState(() {
          _resultText = "API'dan cevap alınamadı. Hata kodu: ${response.statusCode}";
        });
      }
    } catch (error) {
      // Hata durumunda hata mesajını yazdır
      print("Hata: $error");
      setState(() {
        _resultText = "Bir hata oluştu: $error";
      });
    } finally {
      setState(() {
        _isLoading = false; // Yükleniyor durumunu sonlandır
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Hasar Algılama"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              // Fotoğrafın gösterileceği ImageView
              _image != null
                  ? Image.file(
                _image!,
                width: 300,
                height: 300,
              )
                  : Container(
                width: 300,
                height: 300,
                color: Colors.grey[300],
                child: Icon(
                  Icons.image,
                  size: 100,
                  color: Colors.grey[800],
                ),
              ),
              SizedBox(height: 20),
              // Yükleniyor göstergesi
              _isLoading ? CircularProgressIndicator() : SizedBox.shrink(),
              SizedBox(height: 20),
              // 1. Tuş: Fotoğraf seçimi
              ElevatedButton(
                onPressed: _pickImage,
                child: Text("Fotoğraf Seç"),
              ),
              SizedBox(height: 20),
              // 2. Tuş: Fotoğrafı API'ye gönder
              ElevatedButton(
                onPressed: _image == null ? null : _sendImageToApi, // Butonu deaktive etme
                child: Text("API'ye Gönder"),
              ),
              SizedBox(height: 20),
              // API sonucu için text alanı
              Text(
                _resultText,
                style: TextStyle(fontSize: 18),
                textAlign: TextAlign.center,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
