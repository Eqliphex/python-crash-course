dinner_guests = ['William Sidis', 'Albert Einstein', 'Von Neumann']

missing_guest =  dinner_guests.pop()
print(missing_guest + " is not coming.")

dinner_guests.insert(0, "Nikola Tesla")


print("You are invited: " + dinner_guests[0])
print("You are invited: " + dinner_guests[1])
print("You are invited: " + dinner_guests[2])