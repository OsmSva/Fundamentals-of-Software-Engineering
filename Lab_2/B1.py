import os
import math

input_filename = input("Введите имя входного файла: ")

if not os.path.exists(input_filename):
    print(f"Файл {input_filename} не найден в папке с программой!")
else:
    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_line = lines[0].split()
    num_locations = int(first_line[0])
    scale = float(first_line[1])

    legs_miles = []
    total_distance = 0.0

    for line in lines[1:]:
        line = line.strip()
        if line:
            legs_miles.append(float(line))
            total_distance += math.ceil(float(line) * 10.0 * scale) / 10

    print("Marchenko Sviatozar")
    print("Simple Map Distance Computations")
    print()
    print(f"Map Scale Factor: {scale:.2f} miles per inch")
    print()
    print("     Map     Mileage")
    print("     Measure Distance")
    print("=========================================================================")
    leg_number = 1
    for miles in legs_miles:
        print(f"# {leg_number}: {miles:<10.1f}   {math.ceil(miles * 10.0 * scale) / 10:<15.1f}")
        leg_number += 1
    print("=========================================================================")
    print(f"Total Distance: {total_distance:.1f} miles")
