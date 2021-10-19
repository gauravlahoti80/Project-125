factors = []
sum = 0
num = int(input("Enter the number: "))
for i in range(1,num):
    if num%i == 0:
        sum = sum + i

if num == sum:
    print("It's a Perfect number.")
else:
    print("It's not a Perfect number")