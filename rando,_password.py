import random
import string

# Визначаємо всі можливі символи, які можуть бути в паролі
characters = string.ascii_letters + string.digits + string.punctuation

# Задаємо довжину паролю
password_length = 24

# Генеруємо пароль
password = ''.join(random.choice(characters) for i in range(password_length))

print(password)
