users = ['marie', 'patrick', 'morten', 'alexis', 'marc']

print("Is users[0} == 'marie'? I predict True")
print(users[0] == 'marie')

print("\nIs len(users) == 5? I predict True")
print(len(users) == 5)

print("\nIs 'patrick' in the list? I predict True")
print('patrick' in users)

print("\nIs 'jacob' not in the list? I predict True")
print('jacob' not in users)

print("\nIs 'marie' and 'morten' in the list? I predict True")
print('marie' and 'morten' in users)

print("\nIs 'Alexis' or 'alexis' in the list? I predict True")
print(('Alexis' in users) or ('alexis' in users))

print("\nIs 'Patrick' in the list? I predict False")
print('Patrick' in users)

print("\nIs len('Patrick') != 7? I predict False")
print(len('Patrick') != 7)

