start = int(input('Enter the initial pendulum amplitude: '))
end = float(input('Enter the final pendulum amplitude: '))
count = 0

while start > end:
    start = start - (start * 0.084)  # Reduce amplitude by 8.4%
    count += 1

print('The pendulum swung', count, 'times')
