#거스름돈
n = 1260
num = 0

list = [500, 100, 50, 10]
for i in list:
    num += n//i
    n = n % i
print(num)