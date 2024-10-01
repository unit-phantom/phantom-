import re

def check_password_strength(password):
    
    if len(password) < 8:
        return "Пароль слишком короткий! Должен быть не менее 8 символов.", 0


    if not re.search(r'\d', password):
        return "Пароль должен содержать хотя бы одну цифру!", 0

   
    if not re.search(r'[a-z]', password):
        return "Пароль должен содержать хотя бы одну строчную букву!", 0

  
    if not re.search(r'[A-Z]', password):
        return "Пароль должен содержать хотя бы одну заглавную букву!", 0

    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Пароль должен содержать хотя бы один специальный символ!", 0

    return "Пароль достаточно сложный!", calculate_password_crack_time(password)

def calculate_password_crack_time(password):
    possible_characters = 0
    

    if re.search(r'[a-z]', password):
        possible_characters += 26  
    if re.search(r'[A-Z]', password):
        possible_characters += 26  
    if re.search(r'\d', password):
        possible_characters += 10  
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        possible_characters += 32  

   
    total_combinations = possible_characters ** len(password)
    
    attempts_per_second = 10**10
    
    time_to_crack_seconds = total_combinations / attempts_per_second
    
    return time_to_crack_seconds

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} секунд"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} минут"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} часов"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} дней"
    else:
        return f"{seconds / 31536000:.2f} лет"

while True:
    password = input("Введите пароль для проверки (или 'q' для выхода): ")
    
    if password.lower() == 'q':
        print("Выход из программы.")
        break

    result, time_to_crack = check_password_strength(password)
    print(result)

    if result == "Пароль достаточно сложный!":
        print(f"Примерное время для взлома пароля: {format_time(time_to_crack)}")
    
    if result == "Пароль достаточно сложный!":
        continue_check = input("Хотите проверить другой пароль? (да/нет): ").lower()
        if continue_check != 'да':
            print("Программа завершена.")
            break
