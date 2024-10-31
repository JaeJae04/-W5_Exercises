# Federal taxes are 23% of your salary every month. You make X amount of money. How much is withheld for taxes?

federal_taxes = 0.23
Salary = 6500

# calculate the amount withheld for taxes 
witheld_money = Salary * federal_taxes

print('Federal taxes withhold $' + format(federal_taxes, '.2f') + ' every month')