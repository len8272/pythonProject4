1 1 2 3 5 8 13 21 34 55
string = input("Введите числа через пробел:")

list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел

print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка