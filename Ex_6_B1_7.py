# Write a Python program to find characters count of a stringwhich are passed as list.
# Input: St=”hello welcome” lst=[“l‟, ‟w‟, ‟m‟, ‟e‟]
# Output:
# l 3
# w 1
# m 1
# e 3

st = input("Enter a string: ")
lst = list(map(str, input("Enter comma-separated letters: ").split(",")))
for i in lst:
    print(f"{i} {st.count(i)}")
