num1=int(input("Enter first number: ")) #allow user input

num2=int(input("Enter second number: ")) #allow user input 

operand=input("Enter the operand: ")#allow user input

#create if statement to allow adaptability with user operand change
if operand=="+":
    print(f"sum: {num1}+{num2}={num1+num2}")
elif operand=="-":
    print(f"difference: {num1}-{num2}={num1-num2}")
elif operand=="*":
    print(f"product: {num1}*{num2}={num1*num2}")
elif operand=="/":
    print(f"quotient: {num1}/{num2}={num1/num2}")
else:
    print("invalid operand") #invalid operand if user inputs non-operand
