answer = input("Pick a number to see if it's a multiple of ten: ")
answer = int(answer)

if answer % 10 == 0:
    print(str(answer) + " is a multiple of ten!")
else:
    print("Sorry! " + str(answer) + " is not a multiple of ten")