prompt = "Enter your age:\n"
prompt += "0 - 2 = free\t3 - 12 = $10\t12 -  = $15"

message = ""
while message != 'quit' || message.isdigit() == True:
    message = input(prompt + "\n")