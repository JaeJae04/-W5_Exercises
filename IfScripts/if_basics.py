#  1. Create two starting variables:
x = 100
y = 20

if x/y == 5:
    x = 1
    print("x divided by y is 5")
else: 
    print("are the variables set up correctly?")
 
 #Question 2:
if x*y == y:
    x = 10
    print("now x times y is y")
else:
    print("Whoops, x equals " + str(x))

#Question 3:
if x < y:
    x = x*2
    print("x is less than y")
else:
    print("uh oh, x is not less than y")

#Question 3:
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

#Question 4:
print("The final value of x is " + str(x) + " and the final value of y is " + str(y))

