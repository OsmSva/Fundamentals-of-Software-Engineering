import os
import math

input_file = input("Введите имя входного файла: ")

if not os.path.exists(input_file):
    print(f"Файл {input_file} не найден в папке с программой!")
else:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"{"Time":<20}{"WC temp":<25}{"WC Effect":<30}")
    print("----------------------------------------------------------------------------------")
    TWCAverage = 0.0
    for line in lines[2:]:
        l = line.split()
        TWC = 35.74 + 0.6125 * float(l[1]) + (0.4275 * float(l[1]) - 35.75) * (float(l[2])**0.16)
        TWCAverage += TWC
        WCI = TWC - float(l[1])
        print(f"{l[0]:<20}{TWC:<25.1f}{WCI:<30.1f}")
    print("----------------------------------------------------------------------------------")
    print(f"The average adjusted temperature, based on {len(lines) - 2} observations, was {TWCAverage / (len(lines) - 2):.1f}")
