#searching element in dictionary 
contacts = [
    {"name": "Ash", "ph": "98765"},
    {"name": "Pra", "ph": "98689"}
]
found=False
search=input("Enter the name:")
for i in contacts:
    if i["name"]==search:
        found=True
        print("Contact Found")
        print("name:",i["name"])
        print("phone no:",i["ph"])
if not found:
    print("not found")
    