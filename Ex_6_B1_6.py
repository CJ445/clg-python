# https://www.hackerrank.com/challenges/string-validators/problem
user_input = input()
outputs = [False, False, False, False, False]
for letter in user_input:
    if letter.isalnum():
        outputs[0] = True
    if letter.isalpha():
        outputs[1] = True
    if letter.isdigit():
        outputs[2] = True
    if letter.islower():
        outputs[3] = True
    if letter.isupper():
        outputs[4] = True
for output in outputs:
    print(output)
