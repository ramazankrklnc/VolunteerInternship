import random
import string

class PasswordGenerator:

    def __init__(self, length=8, include_uppercase=True, include_numbers=True, include_special_chars=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_numbers = include_numbers
        self.include_special_chars = include_special_chars

    def set_options(self, length=None, include_uppercase=None, include_numbers=None, include_special_chars=None):
        " Kullanıcı isteğine göre şifre seçeneklerini ayarlamaya yarıyor "
        if length is not None:
            self.length = length
        if include_uppercase is not None:
            self.include_uppercase = include_uppercase
        if include_numbers is not None:
            self.include_numbers = include_numbers
        if include_special_chars is not None:
            self.include_special_chars = include_special_chars

    def generate_password(self):
        " Şifre oluşturma fonksiyonu "
        characters = string.ascii_lowercase  # Küçük harfler

        if self.include_uppercase:
            characters += string.ascii_uppercase  # Büyük harfler

        if self.include_numbers:
            characters += string.digits  # Sayılar

        if self.include_special_chars:
            characters += string.punctuation  # Özel karaktrler

        # Şifreyi rastgele seçilen karakterlerle oluştur
        password = ''.join(random.choice(characters) for _ in range(self.length))

        return password


# Örnek kullanım:
generator = PasswordGenerator(length=32, include_uppercase=True, include_numbers=True, include_special_chars=True)
print("Oluşturulan Şifre: ", generator.generate_password())

# Parametreleri değiştirmek isterseniz bu methodu kullanın:
generator.set_options(length=24, include_special_chars=False)
print("Yeni Şifre: ", generator.generate_password())
