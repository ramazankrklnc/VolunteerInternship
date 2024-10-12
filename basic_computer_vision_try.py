import cv2
import matplotlib.pyplot as plt

# Resmi yükle
image = cv2.imread("denemeci0.jpg")

# OpenCV BGR formatını RGB'ye çevir
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Matplotlib ile görüntüyü göster
plt.imshow(image_rgb)
plt.axis('off') 
plt.show()

# 3. Resmi ters çevirme (Y ekseni etrafında)
flipped_image = cv2.flip(image, 1)  # 1, Y ekseninde çevirir
cv2.imshow('Ters Çevrilmiş Resim', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Resmi siyah-beyaz hale getirme (Grayscale)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Siyah-Beyaz Resim', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Resimleri kaydetme
cv2.imwrite('flipped_image.jpg', flipped_image)  # Ters çevrilmiş resmi kaydet
cv2.imwrite('gray_image.jpg', gray_image)  # Siyah-beyaz resmi kaydet
 

 