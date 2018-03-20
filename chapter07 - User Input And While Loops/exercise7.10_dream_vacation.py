question_one = "\nWhat is your name? "
question_two = "If you could visit one place in the world, where would you go? "
question_three = "Would you like to let another person respond? (yes/no) "

answers = {}


#  Set a flag to indicate that polling is active.
is_active = True

while is_active:
    #  Prompt for the person's name and answer.
    name = input(question_one)
    answer = input(question_two)

    #  Store the response in the dictionary: answers[key] = value
    answers[name] = answer

    #  Find out if anyone else is going to take the poll.
    repeat = input(question_three)
    if repeat == 'no':
        polling_active = False

    #  Polling complete. Show the results.
    print("\n--- Poll Results ---")
    for name, answer in answers.items():
        print(name.title() + " would like to visit " + answer.title() + ".")