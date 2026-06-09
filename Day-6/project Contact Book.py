#creating a contct book 
contacts=[]
contact={
            "Name":"Ash",
            "Age":19,
            "Number":98760
}
contact1={
            "Name":"Pradeep",
            "Age":20,
            "Number":56849
}
contacts.append(contact)
contacts.append(contact1)
menu=int(input("Enter the choice:"))
if menu==1:
    print("1. To Add an Element in the list")
    name=input("Enter the name to be added :")
    age=int(input("Enter the age: "))
    number=int(input("Enter the no :"))
    contact2={
                "Name":name,
                "Age":age,
                "Number":number
    }
    contacts.append(contact2)
    for i in contacts:
        print("name:",i["Name"])
        print("Age:",i["Age"])
        print("phone no:",i["Number"])
         
elif menu==2:
    print("2. View Contact")
    for i in contacts:
        print("name:",i["Name"])
        print("Age:",i["Age"])
        print("phone no:",i["Number"])
elif menu==3:
    print("3.search an Element")
    search_element=input("Enter the value to be searched :")
    found=False
    for i in contacts:
        if (i["Name"] == search_element or
            str(i["Age"]) == search_element or
            str(i["Number"]) == search_element
             ):
            found=True
            print("Name :",i["Name"])
            print("Age :",i["Age"])
            print("Number :",i["Number"])
    if not found:
            print("No Match Found")

elif menu==4:
    print("4. Delete an element")
    delete_element=input("Enter the value to be deleted :")
    found=False
    for i in contacts:
        if (i["Name"] == delete_element or
            str(i["Age"]) == delete_element or
            str(i["Number"]) == delete_element
             ):
            found=True
            contacts.remove(i)
    if not found:
        print("Contact not Found")
    for j in contacts:
            print("Name :",j["Name"])
            print("Age :",j["Age"])
            print("Phone No:",j["Number"])
elif menu==5:
    print("Exit")
else:
    print("entered a non existing choice")