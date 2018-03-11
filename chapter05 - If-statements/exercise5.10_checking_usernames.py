current_users = ['admin', 'mmat', 'eqliphex', 'jepla', 'hholm']
new_users = ['aalbert', 'eqliphex', 'pwm', 'lam', 'gretenkort']

for user in new_users:
    if user.lower() in current_users:
        print("Sorry " + user + ", that username is already taken!")
    else:
        print("username is available")
