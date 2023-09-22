# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Python.

arr = [1, 2, 3 ,4]
target = 3
# for item in arr:
#     if (target == item):
#         print('true')
#     else:
#         print('false')

print('solution 1 - search_imperative')
def search_imperative(array, n):
    for number in array:
        if number  == n:
            return True
    return False

print(search_imperative(arr, target))

print('solution 2 -search_declarative')
def search_declarative(arr, num):
    return num in arr

print(search_declarative(arr, target))

