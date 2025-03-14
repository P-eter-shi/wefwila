"""
Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) and the discount 
percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
Print the final price after applying the discount, or if no discount was applied, print the original price.
"""
def calculate_discount(price, discount_percentage):
    #price=price-(price*discount_percentage/100)
    if discount_percentage>=20:
       return price-(price*discount_percentage/100)
    else:
        return price

try:
    original_price=float(input("Enter the original price:"))#allow user input of original price
    discount_percentage=float(input("Enter the discount percentage:"))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    print(f"The final price after discount is: ksh{final_price:.2f}")#print the final price after discount
except ValueError:
    print("Please enter valid numbers.")

    
    