a=int(input("enter number1: "))
b=int(input("enter number2: "))
c=int(input("enter number3: "))
avg= (a+b+c)/3
print("avg= ",avg)
if avg>a and avg>b and avg>c:
    print("avg is greater than 3 given numbers: ")
elif avg>a and avg>b:
    print("avg is greater than only 2 given numbers")
elif avg>a and avg>c:
    print("avg greater than 2 given numbers")
elif avg>b and avg>c:
    print("avg greater than 2 numbers only")
elif avg>a:
    print("avg greater than a")
elif avg>b:
    print("avg greater than b")
elif avg>c:
    print("avg greater than c")
else:
    print("Invalid input")