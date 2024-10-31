# How many vans do you need? How much will it cost to rent vans? What is the cost if you split it per person?

import math 
van_seats = 15
days = 1
tourists = 38
van_rent = 250

# how much will it cost to rent vans 

import math
vans_cost = format(van_rent * tourists) *days

# how many vans are needed?
vans_needed = tourists/van_seats

# What is the cost if you split it per person?
cost_per_person = format(float(vans_cost)/tourists, '.2f')

print(vans_needed)
print(vans_cost)
print(cost_per_person)
print('With ' + str(tourists) + ' tourists we need ' + str(vans_needed) + ' vans which will cost a total of $' + vans_cost + ' which brings it to $' + cost_per_person + ' per person')

# With 38 tourists we need 3 vans which will cost a total of $9500 which brings it to $250.00 per person