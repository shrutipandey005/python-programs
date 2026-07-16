n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

for i in range(n):
    for j in range(0, n-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted list:", lst)
