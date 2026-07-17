r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

matrix = []

for i in range(r):
    matrix.append(list(map(int, input().split())))

print("Transpose:")

for i in range(c):
    for j in range(r):
        print(matrix[j][i], end=" ")
    print()
