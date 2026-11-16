num1 = float(input("Please enter a number: "))
opr = input("Please enter one of the options: +, -, *, /: ")
num2 = float(input("Please enter a number: "))

if opr== "+":
    print(num1+num2)
elif opr== "-":
    print(num1-num2)
elif opr== "*":
    print(num1*num2)
elif opr== "/":
    print(num1/num2)
else:
    print("Invalid operation")

