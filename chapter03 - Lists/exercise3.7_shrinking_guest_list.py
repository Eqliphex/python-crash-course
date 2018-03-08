dinner_guests = ['William Sidis', 'Albert Einstein', 'Von Neumann']

missing_guest =  dinner_guests.pop()
print(missing_guest + " is not coming.")

dinner_guests.insert(0, "Nikola Tesla")


print("You are invited: " + dinner_guests[0])
print("You are invited: " + dinner_guests[1])
print("You are invited: " + dinner_guests[2])

print("Found a bigger table!!!")

dinner_guests.insert(0, "oLgA")

half_size = len(dinner_guests) / 2
dinner_guests.insert(int(half_size), "Tobias Gretenkort")

dinner_guests.append("David Lam")
print(half_size)
print(dinner_guests)

#  new for exercise 3.7

print("I can only have two people with me")

print("Sorry " + dinner_guests.pop() + ", i can't have you at my party")
print("Sorry " + dinner_guests.pop() + ", i can't have you at my party")
print("Sorry " + dinner_guests.pop() + ", i can't have you at my party")
print("Sorry " + dinner_guests.pop() + ", i can't have you at my party")
print(dinner_guests)

print("You are still invited " + dinner_guests[0])
print("You are still invited " + dinner_guests[1])
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
