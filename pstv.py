def print_positive_numbers(start, end):
    for i in range(start, end + 1):
        if i > 0:
            print(i)

start = int(input("Enter start of the range: "))
end = int(input("Enter end of the range: "))

print("Positive numbers in the range:")
print_positive_numbers(start, end)