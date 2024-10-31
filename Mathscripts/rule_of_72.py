# Divide 72 by the annual rate of return 
from tokenize import Double


interest_rate = 5
years_to_double = 72 / interest_rate

print("At a " + str(format(interest_rate, "0.0%")) +  " interest rate, your savings account will be worth " + str(format(Double, ".2f")) + " in " + str(format(years_to_double, ".1f")))