# define a dictionary that includes the following keys and the sample values of your choice:
address_dictionary  = {
    'name': 'Jaela Johnson',
    'address': '112 Ocean Ave',
    'city': 'chicago',
    'state': 'Illinois',
    'zip': '60007'
}

print(f"""{address_dictionary['name']}
{address_dictionary['address']}
{address_dictionary['city']},
{address_dictionary['state']},
{address_dictionary['zip']}""")


del address_dictionary['name']

full_name = (
    {'first_name': 'Freddy'},
    {'last_name': 'Krueger'}
)

address_dictionary.update({'honorific': 'Mr.'})
address_dictionary.update({'first_name': 'Freddy'})
address_dictionary.update({'last_name': 'krueger'})


print(f"""{address_dictionary['honorific']} {address_dictionary['first_name']} {address_dictionary['last_name']}
{address_dictionary['address']}
{address_dictionary['city']},
{address_dictionary['state']} {address_dictionary['zip']}""")