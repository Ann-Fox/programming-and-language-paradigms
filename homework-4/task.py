# '''Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
# ● Формула корреляции Пирсона:
#  Корреляция Пирсона обозначается символом ρ (ро) и вычисляется следующим образом:

# ρ(X,Y) = (Σ((X_i - 𝜇_X)(Y_i - 𝜇_Y))) / (√(Σ(X_i - 𝜇_X)^2) * √(Σ(Y_i - 𝜇_Y)^2))

# где X и Y - массивы случайных величин, 
# Σ означает сумму всех элементов из заданного диапазона,
# 𝜇_X и 𝜇_Y - средние значения массивов X и Y соответственно.

# Формула состоит из двух частей: числителя и знаменателя. 
# В числителе мы вычисляем сумму произведений отклонений каждой пары значений (X_i - 𝜇_X) и (Y_i - 𝜇_Y). 
# Знаменатель представляет собой произведение стандартных отклонений каждого массива. 
# Корреляция Пирсона - это отношение числителя к знаменателю, нормализованное на значения массивов X и Y.

# Значение корреляции Пирсона может варьироваться от -1 до 1. 
# Коэффициент +1 означает положительную линейную связь между массивами, -1 означает отрицательную линейную связь, 
# а 0 означает отсутствие связи.

import math

def pearson_correlation(X, Y):
    if len(X) != len(Y):
        raise ValueError("Массивы X и Y должны иметь одинаковую длину")

    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n
    
    numerator = sum(map(lambda x, y: (x - mean_X) * (y - mean_Y), X, Y))
    denominator = math.sqrt(sum(map(lambda x: (x - mean_X)**2, X))) * math.sqrt(sum(map(lambda y: (y - mean_Y)**2, Y)))
    
    if denominator == 0:
        raise ValueError("Знаменатель равен нулю, деление на ноль невозможно")
    
    return numerator / denominator


X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]
correlation = round(pearson_correlation(X, Y), 2)
print(correlation) # 1.0


# Массивы разной длины
# '''
# X = [1, 2, 3, 4, 5]
# Y = [2, 4, 6, 8]  
# correlation = pearson_correlation(X, Y) #ValueError: Массивы X и Y должны иметь одинаковую длину
# print(correlation)
# '''