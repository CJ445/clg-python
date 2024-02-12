# Write a Python program to remove duplicate elements in a list.
l1 = [ 1, 2, 2, 4, 4, 5,5,5, 6]
l0 = []
for i in l1:
    if i not in l0:
        l0.append(i)
print(l0)
