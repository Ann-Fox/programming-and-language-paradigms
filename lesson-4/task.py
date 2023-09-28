# Контекст
# Есть такая операция в статистике - “нормализация”. Это операция принимающая на вход вектор и возвращающая другой вектор. Смысл этой операции в том, чтобы данные из разных шкал загнать в единый диапазон, как правило - от 0 до 1, тогда с данными становится проще работать.

# Ваша задача
# Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
# x_norm - нормализованное значение элемента
# x - исходное значение элемента
# x_max, x_min - максимальное и минимальное значение в массиве
# x_norm = (x - min_el)/(max_el - min_el)

print("Task 1")

arr = [1, 5, 7, 8, 10]

max_el = max(arr)

def normalaize(arr):
    max_el = max(arr)
    min_el = min (arr)
    def norm_el(x):
        return (x - min_el)/(max_el - min_el)
    
    return list(map(norm_el, arr))

print(normalaize(arr))

# Контекст
# Предположим, что есть какой-то массив содержащий данные о разных людях и их возрасте и вас попросили ответить на следующий вопрос: “сколько в массиве людей возраста > 30?”. Для этого, вы хотите написать программу для фильтрации наблюдений по возрастному признаку.

# Ваша задача
# Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий число - количество людей старше указанного возраста.

# Решение.. ?
print("Task 2")

arr1 = [1, 5, 31, 55, 41, 12, 58, 33]
n = 30

def count_person(arr, n):
    return list(filter(lambda x: x > n, arr))

print(len(count_person(arr1, n)))


# Контекст
# Важнейшая задача в анализе данных - поиск дубликатов. Дубликат - это наблюдение, встречающееся в данных больше одного раза. Такие наблюдения не просто не улучшают результат анализа или полученных моделей, но и замедляют весь процесс в целом, поэтому аналитики и разработчики предпочитают избавляться от них перед тем как приступить к анализу.

# Ваша задача
# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к массиву, дубликаты должны быть выведены на экран в виде списка.

# Решение.. ?
print("Task 3")

arr2 = [1, 5, 4, 1, 9, 7, 8, 6, 1]
def double_data(arr2):
    one_set = set()
    return list(filter(lambda x: x in one_set or one_set.add(x), arr2))

print(double_data(arr2))
