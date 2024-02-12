num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10

if num == rev:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a pallindrome number")
