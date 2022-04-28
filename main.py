def hello_max(say, *args):
    print(say, args)


hello_max('Hello', 'gandon', 'sddd')


def get_name(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_name(Name="Jony", Age='20')

global_var = 1


def print_glob():
    local_var = 100
    print(local_var)
    print(global_var)


print_glob()


def some_f():
    return 10


result = some_f()
print(result)

a = some_f
print(a)
print(type(a))
print(type(a()), a())


def filter_nums(fnumbers, func):
    f_result = []
    for number in fnumbers:
        if func(number):
            f_result.append(number)
    return f_result


numbers = [1, 2, 3, 4, 5, 6, 7]


def is_even(number):
    return number % 2 == 0


def is_not_even(number):
    return number % 2 != 0


def big_four(number):
    return number > 4


print(filter_nums(numbers, lambda number: number > 4))

print(filter_nums(numbers, lambda number: number % 2 == 0))

print(filter_nums(numbers, lambda number: number % 2 != 0))

numbers = [1, 3, 5, 3, 7, 12, 56]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

cities = [('Moscow', 1000), ('Las Vega', 500), ('Piter', 1200)]

print(sorted(cities, key=lambda city: city[1]))

number_k = (1, 2, 3, 4, 5, 6, 7, 10)
result = filter(is_even, number_k)
print(result)
result = list(result)
print(result)

names = ['Max', 'Kate', 'Leo']
print(list(filter(lambda x: len(x) == 3, names)))

number_3_less = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, number_3_less)))


def max_d(*args):
    return max(args)


print(max_d(23, 45, 3, 100, 12))


person_a = {"name": "Jony", "Health": 50, 'Damage': 23}
person_b = {"name": "bob", "Health": 100, 'Damage': 12}


def person(name, age, city):
    return '{}, {} год(а), прожимает в городе {}'.format(name, age, city)


print(person('Василий', 21, 'Москве'))


def attack(perc1, perc2):
    print(perc1['Health'] - perc2['Damage'])
    print(perc2['Health'] - perc1['Damage'])
    perc1['Health'] = perc1['Health'] - perc2['Damage']
    print(perc1)


attack(person_a, person_b)



