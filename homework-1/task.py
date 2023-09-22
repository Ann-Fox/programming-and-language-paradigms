# Task 1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

array_num = [6, 2, 0, 4, 8, 3, 1] 

def sort_imperative(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

sort_imperative(array_num)
print(array_num)  

# Task №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_declarative(array):
    return sorted(array, reverse=True)

print(sort_declarative(array_num)) 

# [8, 6, 4, 3, 2, 1, 0]