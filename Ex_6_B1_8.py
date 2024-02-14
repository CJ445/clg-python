# Write a Python program to find the first appearance of the substring 'not' and 'bad'
# from a given string, if 'not' follows the 'bad', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string.
# Sample Input :
# The song is not that bad!
# The song is poor!
# Sample Output:
# The song is good!
# The song is poor!

t = int(input("No. of test cases: "))
for i in range(t):
    s = input("Enter text: ")
    if "not" in s and "bad" in s:
        ind = s.find("not")
        s = s.replace("not","good")
        print(s[:ind+4]+"!") # prints till the last i.e. 4th letter of the word 'good'. Since .find('not') return index position of 'n'.
    else:
        print(s)
