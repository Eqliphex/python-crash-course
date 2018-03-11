alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#  Initializing an empty dictionary and filling it:
alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

print(alien_1)

#  Overwriting an entry:
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


#  A more complex example:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#  Move the alien to the right.
#  Determine how for to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

#  The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))

#  Deleting a key/value pair:
del alien_0['x_position']
print(alien_0)