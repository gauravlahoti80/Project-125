factors = []
num = int(input("Enter the number: "))
for i in range(1,num+1):
    if num%i == 0:
        factors.append(i)

if len(factors) == 2:
    print('It is a prime number')
else:
    print('It is not a prime number')
