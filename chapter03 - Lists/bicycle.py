#  representation of the list:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#  accessing an element in the list:
print(bicycles[0])
print(bicycles[0].title())

#  accessing last element in list:
print(bicycles[-1])
print(bicycles[-1].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)