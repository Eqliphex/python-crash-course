poll_candidates = ['jen', 'sarah', 'edward', 'phil', 'patrick', 'khalid',
                   'morten', 'jacob', 'mathias']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

for candidate in poll_candidates:
    if candidate in favorite_languages:
        print("Thank you for helping " + candidate.title())
    else:
        print("You should help us " + candidate.title())
