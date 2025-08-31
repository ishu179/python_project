# Calculate Factorial Using a Function
def factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1

    for i in range(2, x + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
