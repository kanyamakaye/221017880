a= int(input("How many friends are going to take dinner "))
if a<=0:
 print("No one is going to join party here")
else:
 friends={}
print("Enter names of friend going to take dinner\n")
friend_dict = {}

for i in range(a):
    name = input(f"give the name of friend you want {i+1}: ")
    friend_dict[name] = 0

friend_dict["You"] = 0

print("Friend dictionary:", friend_dict)