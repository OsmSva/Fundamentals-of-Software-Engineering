import string


password = input()
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
b = True




if len(password) != 8:
    b = False
    print("Длина пароля не равна 8")
if password == password.lower():
    b = False
    print("В пароле отсутствуют заглавные буквы")
if password == password.upper():
    b = False
    print("В пароле отсутствуют строчные буквы")
if all(symbol in allowed for symbol in password) == False:
    b = False
    print("В пароле используются непредусмотренные символы")
if any(symbol.isdigit() for symbol in password) == False:
    b = False
    print("В пароле отсутствуют цифры")
if any(symbol == '*' or symbol == '-' or symbol == '#' for symbol in password) == False:
    b = False
    print("В пароле отсутствуют специальные символы")
    
    
    
    
    
if b == True:
    print("Надежный пароль")
