friend_list = ['morten struckmann', 'tobias gretenkort', 'hendrik holm', 'david lam', 'dennis frost', 'marc christensen']

print("The first three items are:")
print(friend_list[0:3])

friend_list_median = int(len(friend_list) / 2)
print("The items in the middle:")
print(friend_list[friend_list_median-1:friend_list_median+2])

print("The last three items in list:")
print(friend_list[-3:])