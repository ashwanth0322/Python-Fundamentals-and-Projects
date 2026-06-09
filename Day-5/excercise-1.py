#searching an element in the list 
list=[90,80,95]
search_item=80
item=False
for i in list:
    if i != search_item:
        item=False
if item == True:
    print("Found")
else:
    print("Not Found")

    
    
