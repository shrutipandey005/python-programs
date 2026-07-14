str1 = input("Enter string: ")
count = 0

for ch in str1:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Vowels =", count)
