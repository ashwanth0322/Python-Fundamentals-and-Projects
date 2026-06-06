#create a  contact book using list and dictionary 
contacts=[]
contact={
            "name":"Ash",
             "ph":"98765"
}
contact1={
            "name":"pra",
            "ph":98689
}
contacts.append(contact)
contacts.append(contact1)
for i in contacts:
    print("name:",i["name"])
    print("phone no:",i["ph"])