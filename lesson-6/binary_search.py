# Написать программу в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

def binary_search(arr, left, right, n):
    if left > right:
        return -1    
    mid = (left + right) // 2    
    if arr[mid] == n:
        return mid
    elif arr[mid] < n:
        return binary_search(arr, mid + 1, right, n)
    else:
        return binary_search(arr, left, mid - 1, n)


arr1 = [2, 4, 6, 8, 10, 12, 14]
n = 5
print(binary_search(arr1, 0, len(arr1)-1, n))