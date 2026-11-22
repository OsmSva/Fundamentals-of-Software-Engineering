s = input()

if len(s) < 5:
    print("Ошибка: длина строки должна быть не меньше 5 символов!")
else:
    is_valid = True
    for ch in s:
        if ch != "0" and ch != "1":
            is_valid = False
            break

    if not is_valid:
        print("Ошибка: используйте только символы '0' и '1'!")
    else:
        total = len(s)
        lost = 0
        max_zero = 0
        cur_zero = 0
        for ch in s:
            if ch == "0":
                lost += 1
                cur_zero += 1
                if cur_zero > max_zero:
                    max_zero = cur_zero
            else:
                cur_zero = 0
  
        percent = (lost / total) * 100

        if percent <= 1:
            quality = "отличное качество"
        elif percent <= 5:
            quality = "хорошее качество"
        elif percent <= 10:
            quality = "удовлетворительное качество"
        elif percent <= 20:
            quality = "плохое качество"
        else:
            quality = "критическое состояние сети"

        print(f"Общее количество пакетов: {total}")
        print(f"Количество потерянных пакетов: {lost}")
        print(f"Длина самой длинной последовательности потерянных пакетов: {max_zero}")
        print(f"Процент потерь: {percent:.1f}%")
        print(f"Качество связи: {quality}")
