user_names = ['eqliphex', 'jepla', 'mmat', 'admin', 'hbom', 'pwm']

for user in user_names:
    if user == 'admin':
        print("Hello admin!, would you like a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again!")