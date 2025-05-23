def d(x):
    return x**3 - 3 * x**2 - 12 * x + 10  # Danger level function

D = float(input('Enter the maximum allowable danger level: '))

while D < 0:
    D = float(input('Enter a positive number: '))

l, r, x_min, D_min = 0, 4, 4, D

while (r - l) >= 1e-8:
    x = (l + r) / 2
    if d(x) < -D:
        r = x
    else:
        l = x
        if abs(d(x)) < abs(D_min):
            x_min, D_min = x, d(x)

print('Approximate depth of safe laying:', x_min, 'm')
