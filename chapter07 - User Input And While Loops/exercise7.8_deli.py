sandwich_orders = ['beef sandwich', 'cheese sandwich', 'veggie sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title())
    finished_sandwiches.append(current_sandwich)

print("All sandwiches has been made!")
