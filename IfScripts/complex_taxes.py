# Create a script  that will calculate federal tax based on the values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

from calendar import Day


pay_rate = 21.50
hours_worked = 30
regular_hours = 40
overtime = 1.5

if hours_worked <= regular_hours:
    gross_pay = pay_rate*hours_worked
    print("You are not eligible for overtime pay work harder. Your gross pay calculates to $" + str(format(gross_pay, ".2f")))
elif hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    print(" You are eligible for overtime pay You have made an additional $" + 
          str(format(overtime_hours*pay_rate*overtime, ".2f")) + 
          " Your total gross pay is $" + 
          str(format((regular_hours*pay_rate)+(overtime_hours*pay_rate*overtime), ".2f")))
    
    weeks_worked = float(input("Please enter the number of weeks worked for the year: "))
filer_status = str(input("Please enter your filing status (Single/Joint): ").lower())


# Calculate the unknown
if gross_pay < 12000 and filter == 'single':
    fed_tax = round((gross_pay * .05) / 52, 2)
elif gross_pay < 12000 and filter == 'joint':
    fed_tax = 0
elif gross_pay < 24999.99 and filter == 'single':
    fed_tax = round((gross_pay * .1) / 52, 2)
elif gross_pay < 24999.99 and filter == 'joint':
    fed_tax = round((gross_pay * .06) / 52, 2)
elif gross_pay < 74999.99 and filter == 'single':
    fed_tax = round((gross_pay * .15) / 52, 2)
elif gross_pay < 74999.99 and filter == 'joint':
    fed_tax = round((gross_pay * .11) / 52, 2)
else:
    fed_tax = round((gross_pay * .2) / 52, 2)

# Display the results
print(f'''
      You worked {hours_worked} hours this period
      Because you earn ${pay_rate} per hour, your gross weekly pay is ${Day + overtime_hours} 
      Your filing status is {filter}
      Your tax withholding for the week is ${fed_tax}
      Your net pay is {Day + overtime_hours - fed_tax}
      ''')


# Same code copied with all values needing an input to test different values
# Define known values
pay_rate = float(input())
hours_worked = int(input())
filer = input('single or joint? ')
pay = round(40 * pay_rate, 2)
gross_pay = round(overtime_hours + pay, 2) if hours_worked > 40 else round(hours_worked * pay_rate, 2)
ot_pay = round((hours_worked - 40) * (pay_rate * 1.5), 2)


# Calculate the unknown
if gross_pay < 12000 and filer == 'single':
    fed_tax = round((gross_pay * .05) / 52, 2)
elif gross_pay < 12000 and filer == 'joint':
    fed_tax = 0
elif gross_pay < 24999.99 and filer == 'single':
    fed_tax = round((gross_pay * .1) / 52, 2)
elif gross_pay < 24999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .06) / 52, 2)
elif gross_pay < 74999.99 and filer == 'single':
    fed_tax = round((gross_pay * .15) / 52, 2)
elif gross_pay < 74999.99 and filer == 'joint':
    fed_tax = round((gross_pay * .11) / 52, 2)
else:
    fed_tax = round((gross_pay * .2) / 52, 2)

print(f'''
      You worked {hours_worked} hours this period
      Because you earn ${pay_rate} per hour, your gross weekly pay is ${gross_pay}
      Your filing status is {filer}
      Your tax withholding for the week is ${fed_tax}
      Your net pay is {gross_pay - fed_tax}
      ''')

# Display results You are not eligible for overtime pay work harder. Your gross pay calculates to $645.00 Please enter your filing status (Single/Joint):