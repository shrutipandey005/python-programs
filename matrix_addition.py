r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

A = []
B = []

print("Enter matrix A:")
for i in range(r):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter matrix B:")
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Result:")
for i in result:
    print(i)
