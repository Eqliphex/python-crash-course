players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3]) #  first param inclusive, second param non inclusive

print(players[1:4])

print(players[:4]) #  Takes from the start of the list, if first param is omitted.

print(players[2:]) #  Takes to the end of second param is omitted.

print(players[-3:]) #  Takes from the 3 last element and forward.

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
