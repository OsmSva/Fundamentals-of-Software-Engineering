def rect(n, m, s):
    for i in range(n):
        print(s * m)

def triangle(n, s):
    for i in range(1, n + 1):
        print(s * i)

def frame(n, m, s):
    for i in range(n):
        if i == 0 or i == n - 1:
            print(s * m)
        else:
            print(s + " " * (m - 2) + s)

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))
sym = "#"
print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
rect(n, m, sym)
print("\nПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК:")
triangle(n, sym)
print(f"\nРАМКА {n}x{m}:")
frame(n, m, sym)
