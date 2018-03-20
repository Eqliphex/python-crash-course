sandwich_orders = ['beef sandwich', 'pastrami sandwich', 'cheese sandwich',
                   'pastrami sandwich', 'veggie sandwich', 'pastrami sandwich']
finished_sandwiches = []

print(sandwich_orders)

#  Checks to see of 'pastrami sandwich' is in the list.
if 'pastrami sandwich' in sandwich_orders:
    print("Sorry the deli has run out of pastrami!")

#  Removing the item 'pastrami sandwich' from list.
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

#  'Makes' the sandwiches in the list sandwich_orders.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

print("All sandwiches has been made!")
