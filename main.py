def hello_max(say, *args):
    print(say, args)


hello_max('Max', 'gandon', 'sddd')


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


def filter_nums(fnumbers):
    f_result = []
    for number in fnumbers:
        if number % 2 == 0:
            f_result.append(number)
    return f_result


numbers = [1, 2, 3, 4, 5, 6, 7]
print(filter_nums(numbers))


