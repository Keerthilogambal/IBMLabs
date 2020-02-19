num = int(input("enter number"))
factorial = 1
if num < 0:
    print("the number is less than zero")
elif num == 0:
    print("the number is equal to zero")
else:
    for i in range (1 , num+1):
        factorial = factorial * i


print(factorial)