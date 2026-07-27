search = input("Enter name to search: ")

file = open("students.txt", "r")

found = False

for line in file:
    data = line.split()
    if data[0] == search:
        print("Found:", line.strip())
        found = True
        break

if not found:
    print("Not found")

file.close()
