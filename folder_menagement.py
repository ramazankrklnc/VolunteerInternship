import os

class FileManager:

    def __init__(self, directory='.'):
        self.directory = directory  # Varsayılan dizin

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.directory, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Klasör oluşturuldu: {folder_path}")
        except FileExistsError:
            print(f"Klasör zaten mevcut: {folder_path}")

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.directory, folder_name)
        try:
            os.rmdir(folder_path)
            print(f"Klasör silindi: {folder_path}")
        except FileNotFoundError:
            print(f"Klasör bulunamadı: {folder_path}")
        except OSError:
            print(f"Klasör boş değil veya silinemiyor: {folder_path}")

    def create_file(self, file_name, content=""):
        file_path = os.path.join(self.directory, file_name)
        # Dosya yolu klasörünü kontrol et ve yoksa oluştur
        folder = os.path.dirname(file_path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Dosya oluşturuldu: {file_path}")

    def edit_file(self, file_name, content):
        file_path = os.path.join(self.directory, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(content)
            print(f"Dosya düzenlendi: {file_path}")
        else:
            print(f"Dosya bulunamadı: {file_path}")

    def delete_file(self, file_name):
        file_path = os.path.join(self.directory, file_name)
        try:
            os.remove(file_path)
            print(f"Dosya silindi: {file_path}")
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {file_path}")

# Kullanıcı girişlerine göre işlemleri döngü ile yöneten kısım
manager = FileManager(directory='./my_directory')  # Belirli bir dizin ayarla

while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1. Klasör oluştur")
    print("2. Dosya oluştur")
    print("3. Dosya düzenle")
    print("4. Dosya sil")
    print("5. Klasör sil")
    print("6. Çıkış")

    choice = input("Seçiminizi yapın (1-6): ")

    if choice == '1':
        folder_name = input("Klasör adını girin: ")
        manager.create_folder(folder_name)

    elif choice == '2':
        file_name = input("Dosya adını girin (klasörle birlikte örn: 'example_folder/example_file.txt'): ")
        content = input("Dosyaya yazmak istediğiniz içeriği girin: ")
        manager.create_file(file_name, content)

    elif choice == '3':
        file_name = input("Düzenlemek istediğiniz dosyanın adını girin: ")
        content = input("Dosyaya eklemek istediğiniz içeriği girin: ")
        manager.edit_file(file_name, content)

    elif choice == '4':
        file_name = input("Silmek istediğiniz dosyanın adını girin: ")
        manager.delete_file(file_name)

    elif choice == '5':
        folder_name = input("Silmek istediğiniz klasör adını girin: ")
        manager.delete_folder(folder_name)

    elif choice == '6':
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
