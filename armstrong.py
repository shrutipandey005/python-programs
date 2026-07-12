num = int(input("Enter number: "))
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit * digit * digit
    num = num // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
