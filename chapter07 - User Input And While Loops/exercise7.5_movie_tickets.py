prompt = "Enter your age:\n"
prompt += "0 - 2 = free\t3 - 12 = $10\t12 -  = $15"

message = ''
answer = "Your movie ticket costs"
while not message.isdigit() and message != 'quit':
    message = input(prompt + "\n")

if 0 < int(message) < 2:
    print(answer + " nothing")
elif 2 <= int(message) <= 12:
    print(answer + " $10")
elif 12 < int(message):
    print(answer + " $15")

