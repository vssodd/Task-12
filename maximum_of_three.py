def maximum_of_three(a, b, c):
    max_ab = maximum_of_two(a, b)
    if c > max_ab:
        return c
    else:
        return max_ab

c = int(input('Enter the third number: '))

result_abc = maximum_of_three(a, b, c)

print('The maximum of', a, ',', b, 'and', c, 'is', result_abc)
