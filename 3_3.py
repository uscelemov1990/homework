'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

def max_summ(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + b
    elif c <= a and c <= b:
        return a + b

print(max_summ(1, 2, 3))
