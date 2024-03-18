# Define description and price for the Lovely Loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Define description and price for the Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Define description and price for the Luxurious Lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Define the sales tax rate
sales_tax = 0.088

# Initialize the total cost for Customer One
customer_one_total = 0

# Initialize the itemization list for Customer One
customer_one_itemization = ""

# Add the prices of the Lovely Loveseat and Luxurious Lamp to Customer One's total
customer_one_total += lovely_loveseat_price + luxurious_lamp_price

# Add the descriptions of the Lovely Loveseat and Luxurious Lamp to Customer One's itemization list
customer_one_itemization += lovely_loveseat_description + "\n" + luxurious_lamp_description

# Calculate the sales tax for Customer One
customer_one_tax = customer_one_total * sales_tax

# Add the sales tax to Customer One's total cost
customer_one_total += customer_one_tax

# Print the itemization list for Customer One
print("Customer One Items:")
print(customer_one_itemization)

# Print the total cost for Customer One
print("Customer One Total:")
print(customer_one_total)
