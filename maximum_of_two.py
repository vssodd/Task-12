def maximum_of_two(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

result_ab = maximum_of_two(a, b)

print('The maximum of', a, 'and', b, 'is', result_ab)
