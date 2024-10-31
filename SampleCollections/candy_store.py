# create 3 fruit flavored candies 

candy = ('fruties','jaw breakers','mamba')
flavors = ('cherry', 'pomegranate', 'kiwi')


candy_combos = {flavors[0] +' '+ candy[0],
                flavors[1] +' '+ candy[2],
                flavors[2] +' '+ candy[1]}

print("Today's candy options include:" + str(candy_combos))
# The order of each candy type changes but the flavers stays in their proper candy type.