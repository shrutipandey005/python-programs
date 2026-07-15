n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("List without duplicates:", unique)
