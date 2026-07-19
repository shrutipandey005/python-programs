str1 = input("Enter string: ")

upper = 0
lower = 0

for ch in str1:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase =", upper)
print("Lowercase =", lower)
