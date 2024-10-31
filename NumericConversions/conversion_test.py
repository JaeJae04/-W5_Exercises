# Description: This script tests various numeric 
#              conversion techniques 
# Author: Craig B. Newprogrammer

# Define the following variables:

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a = float(a.strip())
b = int(b)
c = str(c)
d = int(d[7:].strip())
print(a, type(a), b, type(b), c, type(c), d, type(d))

