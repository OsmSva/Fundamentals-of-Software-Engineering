
import random
import time

try:
    n = int(input("Введите количество примеров: "))
except ValueError:
    exit()

correct = 0
total_time = 0

for i in range(1, n + 1):
    a, b = random.randint(2, 9), random.randint(2, 9)
    ans = a * b
    print(f"Вопрос {i}/{n}")
    t0 = time.time()
    while True:
        user_inp = input(f"{a} × {b} = ")
        dt = time.time() - t0

        try:
            val = int(user_inp)
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

        total_time += dt
        if val == ans:
            print(f"Верно! (Время: {dt:.1f} сек)")
            correct += 1
        else:
            print(f"Неверно! Правильно: {ans} (Время: {dt:.1f} сек)")
        break

print("=" * 50 + "\nСТАТИСТИКА:\n" + "=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / n:.1f} сек" if n else 0)
print(f"Правильных ответов: {correct}/{n}")
print(f"Процент правильных: {(correct / n * 100):.1f}%" if n else 0)
