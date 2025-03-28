def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {original_price}")
