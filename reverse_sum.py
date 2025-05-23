N = int(input("Enter the first number: "))
K = int(input("Enter the second number: "))

N_reversed = int(str(N)[::-1])
K_reversed = int(str(K)[::-1])

sum_reversed = N_reversed + K_reversed

sum_reversed_reversed = int(str(sum_reversed)[::-1])

print("\nFirst number reversed:", N_reversed)
print("Second number reversed:", K_reversed)
print("\nSum:", sum_reversed)
print("Sum reversed:", sum_reversed_reversed)
