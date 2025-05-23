def count_numbers(number):
    count = 0
    temp = number
    while temp > 0:
        count += 1
        temp = temp // 10
    return count

def change_number(number):
    last_digit = number % 10
    num_count = count_numbers(number)
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    new_number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return new_number

def main():
    first_n = int(input('Введите первое число: '))
    first_num_count = count_numbers(first_n)

    if first_num_count < 4:
        print('В первом числе меньше четырёх цифр.')
    else:
        first_n = change_number(first_n)
        print('Изменённое первое число:', first_n)

        second_n = int(input('\nВведите второе число: '))
        second_num_count = count_numbers(second_n)

        if second_num_count < 4:
            print('Во втором числе меньше четырёх цифр.')
        else:
            second_n = change_number(second_n)
            print('Изменённое второе число:', second_n)
            print('\nСумма чисел:', first_n + second_n)

main()
