def print_sep(separate='*'):
    print(separate * 100)


print_sep('f')

test_variable = (1, '212', 3, 4, 5)

name = test_variable[1]
print(name, type(name), sep='    ')

for i in range(6):
    print(i)


def get_name(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_name(Name="Jony", Age='20')

a = print_sep

print(a('f'))