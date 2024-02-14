# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Input: red, black, pink, green
# Sample Output: black, green, pink, red

text = list(map(str, input().split(",")))
text = list(set(text))
text.sort()
for i in text:
    print(i, end=",")
