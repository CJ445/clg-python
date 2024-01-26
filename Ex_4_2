# Write a python program to check Armstrong number using functions
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_cubes = 0
    for digit in num_str:
        sum_of_cubes += int(digit) ** num_digits
    if sum_of_cubes == num:
        return True
    else:
        return False
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
