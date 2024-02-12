# Write a python program to print each and every element in reverse order. List of strings - reverse each string.
l2 = ["Cyril", "Abel", "Aarin", "Maharishi"]
rev_l = []
for i in l2:
    rev = i[::-1]
    rev_l.append(rev)
print(rev_l)
