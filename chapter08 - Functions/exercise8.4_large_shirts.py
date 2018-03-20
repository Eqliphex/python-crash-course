def make_shirt(shirt_text='I love Python', shirt_size='large'):
    print("\nThe size of the shirt is: " + shirt_size.title())
    print("And the text on the shirt says:\n\t'" + shirt_text + "'")


make_shirt('this is a small t-shirt', 'small')
make_shirt(shirt_text='some clever quote', shirt_size='medium')
make_shirt(shirt_text='This is grossly overrated...')
make_shirt()