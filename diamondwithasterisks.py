size = int(input("Enter the size >> "))
count = size
for i in range(size):
    print(" " * count, end="")
    for j in range(i + 1):
        print("{0:2}".format("*"), end="")
    print()
    count -= 1
count = 2
for i in range(size-1, -1, -1):
    print(" " * count, end="")
    for j in range(i):
        print("{0:2}".format("*"), end="")
    print()
    count += 1