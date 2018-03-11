banned_users = ['andrew', 'carolina', 'pineapple']
user = 'andrew'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")
else:
    print(user.title() + ", sorry but your account has been banned!")
