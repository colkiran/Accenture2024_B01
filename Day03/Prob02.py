
def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

iter = int(input("Enter the number of Fibanocci numbers to be generated :"))
for i in range(iter):
    print(fibo(i), end=" ")

