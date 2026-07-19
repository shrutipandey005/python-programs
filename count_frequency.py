lst = list(map(int, input("Enter elements: ").split()))

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)
