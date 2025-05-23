number = float(input('Enter a positive number > 0: '))
count = 0

if number >= 10:
    # Normalize number by dividing until it is less than 10
    while number >= 10:
        number /= 10
        count += 1
elif number < 1:
    # Normalize number by multiplying until it is at least 1
    while number < 1:
        number *= 10
        count -= 1

print('Floating point format: x =', round(number, 1), '* 10 **', count)
