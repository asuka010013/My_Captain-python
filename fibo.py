def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

numbers = int(input("Enter the number of terms to be printed: "))

print("Fibonacci series for the given terms is as follows :")
fibonacci(numbers)
