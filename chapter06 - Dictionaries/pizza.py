#  Store information about a pizza being ordered:
#  We can use a list to store more than one value to a single key!
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

# Summarize the order:
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print(">\t" + topping)