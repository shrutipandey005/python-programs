n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if lst[mid] == key:
        found = True
        break
    elif lst[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Found")
else:
    print("Not Found")
