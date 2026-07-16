n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

key = int(input("Enter element to search: "))

if key in lst:
    print("Found")
else:
    print("Not Found")
