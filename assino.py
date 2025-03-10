num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operand=input("Enter the operand: ")
if operand=="+":
    print(f"sum: {num1}+{num2}={num1+num2}")
elif operand=="-":
    print(f"difference: {num1}-{num2}={num1-num2}")
elif operand=="*":
    print(f"product: {num1}*{num2}={num1*num2}")
elif operand=="/":
    print(f"quotient: {num1}/{num2}={num1/num2}")
else:
    print("invalid operand")