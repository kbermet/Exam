# 1
x = int(str(float(5)))
# тип целое число/ integer (неизменяемый)
# 2
x = 'aa' == 'AA'
# логический тип данных boolean
# 3
x = {i: i ** 2 for i in range(5)}
# словарь / dict
# 4
x = set(list((5, 6, 7)))
# тип множество / set
# 5
a = {1: 1, 2: 4, 3: 9}
x = a.get(4)

# Тип данных NoneType
# 6
x = [].append('j')
# Тип данных NoneType
# 7
for i in range(10):
    if i < 5:
        x = 'hello'
    else:
        x = 5
# тип целое число/ integer
# 8
x = input('Enter and integer: ')
# строковый тип данных (неизменяемы)
# 9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b


# изменяемый тип данных список list
# 10
def func(x, y=5):
    return x + y


x = func('Jaguar ', 'hunter')
# строковый тип данных (неизменяемы)
