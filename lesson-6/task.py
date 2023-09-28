# Контекст
# Ещё один известный и довольно эффективный алгоритм сортировки массива - сортировка слиянием (merge sort). Алгоритм делится на два этапа:
# этап разбиения - массив разбивается на пару массивов до тех пор пока, полученные массивы не станут массивами длины 1 (состоящими из одного элемента).
# этап слияния - соединяем пары массивов в большие массивы так, чтобы полученные массивы были отсортированы.


# Ваша задача
# Реализовать сортировку слиянием на любом языке в любой парадигме. На вход ваша программа получает массив из чисел, а вернуть должна отсортированный массив.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]    
    left = merge_sort(left)
    right = merge_sort(right)    
    return merge(left, right)


def merge(left, right):
    arr_merg = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr_merg.append(left[i])
            i += 1
        else:
            arr_merg.append(right[j])
            j += 1
    
    while i < len(left):
        arr_merg.append(left[i])
        i += 1
    
    while j < len(right):
        arr_merg.append(right[j])
        j += 1
    
    return arr_merg

arr = [5, 2, 8, 4, 1, 9, 6, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)