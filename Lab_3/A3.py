
import math

a = int(input())
b = int(input())
total = 0
if b < a:
    total = 9999 - a + b + 1
else:
    total = b - a

total_end = total

pay = 0
if total > 0:
    pay += 21.0
if total > 800:
    pay += (total - 800.0) * 0.025
    total = 800
if total > 600:
    pay += (total - 600.0) * 0.04
    total = 600
if total > 300:
    pay += (total - 300.0) * 0.06
pay = round(pay, 2)
print(f"{'Предыдущее:':<15}   {'Текущее:':<15}   {'Использовано:':<15}   {'К оплате:':<15}   {'Ср. цена m^3:':<15}")
print(f"{a:<15}   {b:<15}   {total_end:<15}   {pay:<15.2f}   {round(pay / total_end, 2):<15.2f}")
