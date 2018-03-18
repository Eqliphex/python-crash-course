prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"

is_active = True #  This is a flag, to tell if all our conditions holds true
message = ""

while is_active:
    message = input(prompt)
    if message == 'quit':
        is_active = False
    else:
        print(message)