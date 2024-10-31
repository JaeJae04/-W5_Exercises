# Define variables for pay rate and hours worked
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