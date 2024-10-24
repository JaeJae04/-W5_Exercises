food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

#Display the results
#print("The total due is " + str(total_due))

#The str() function converts value to a sting type date type, it is used here because the value of total_due is for the print () function.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))

# Bonus- you can't simply copy and past the above text into VSCode because it does not evaluate the string I ended up getting an error for invalid character.

print("Tip is " + format(tip, ".2f"))