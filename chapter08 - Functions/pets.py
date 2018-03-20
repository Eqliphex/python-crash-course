def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


#  Positional arguments - Ordering matters!
describe_pet('buller', 'dog')
describe_pet('mocha', 'cat')

#  Keyword Arguments - We don't need to worry about position.
describe_pet(animal_type='hamster', pet_name='harry')

#  We are using default value in 'animal_type', so we only need one argument
describe_pet(pet_name='juliane')
