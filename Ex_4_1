# Write a python program to check whether a number is a palindrome or not using a function
def is_palindrome(num):
    original_num = num
    reverse_num = 0

    while num > 0:
        digit = num % 10
        reverse_num = (reverse_num * 10) + digit
        num = num // 10

    if original_num == reverse_num:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
