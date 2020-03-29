fibo, fibonacci = 0, 1
count = 0
num = int(input("Enter the number of fibonacci numbers: "))
while count <= num:
    print(fibonacci)
    fibo, fibonacci = fibonacci, fibo + fibonacci
    count += 1