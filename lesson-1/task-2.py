#  Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

arr = [0, 1, -5, 10, -6, 56, 0]
print('solution 1')
def imperative(array):
    numbers = [0, 0, 0]
    for num in array:
        if(num < 0):
            numbers[0] += 1
        elif (num == 0):
            numbers[1] += 1
        elif (num > 0):
            numbers[2] += 1
    print(numbers[0]/len(array))
    print(numbers[1]/len(array))
    print(numbers[2]/len(array))
        
imperative(arr)

print('solution 2')

def declarative(arr):
    pos_cnt = len(list(filter(lambda x: x > 0, arr)))
    neg_cnt = len(list(filter(lambda x: x < 0, arr)))
    zer_cnt = len(list(filter(lambda x: x == 0, arr)))
    counts = [pos_cnt, neg_cnt, zer_cnt]
    return list(map(lambda count: count / len(arr), counts))

print(declarative(arr))