user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin!, would you like a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again!")
else:
    print("We need to find users!")