pizzas = ['gorgonzola pizza', 'chicken pizza', 'meatlover pizza']

for pizza in pizzas:
    print("I like " + pizza)

print("New sentence with i love pizza!")

#  Making a copy of the list to a new one:
friend_pizzas = pizzas[:]

#  Proving they are two different entities:
pizzas.append('cheese pizza')
friend_pizzas.append('cabbage pizza')

print(pizzas)
print(friend_pizzas)