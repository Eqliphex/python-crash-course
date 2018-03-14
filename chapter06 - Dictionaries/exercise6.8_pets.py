buller = {
    'owner': 'patrick',
    'type': 'dog',
    }

juliane = {
    'owner': 'inger',
    'type': 'dog',
    }

sissi = {
    'owner': 'inger',
    'type': 'dog',
}

sasja = {
    'owner': 'patrick',
    'type': 'dog',
}

mokka = {
    'owner': 'patrick',
    'type': 'cat',
}

pets = [buller, juliane, sissi, sasja, mokka]

for pet in pets:
    for name, info in pet.items():
        print(name + " " + info)