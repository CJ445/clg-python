num = int(input('Enter a number to find the factorial: '))
fact, i = 1, 1
while i <= num:
    fact = fact * i
    i = i + 1
print(f"The factorial of {num} is {fact}")
