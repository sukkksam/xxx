import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase  

    if use_uppercase:
        characters += string.ascii_uppercase  
    if use_numbers:
        characters += string.digits  
    if use_special_chars:# добавляем специальные символы

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Введите длину пароля: "))
    password = generate_password(length=password_length)
    print(f"Сгенерированный пароль: {password}")