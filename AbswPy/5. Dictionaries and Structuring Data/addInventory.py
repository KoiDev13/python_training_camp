def displayInventory(inventory):
    total_items = 0 
    for item, quantity in inventory.items():
        print(str(quantity)+' '+item)
        # total_items =+ quantity
        total_items += quantity
    print("Total numbers of items " + str(total_items))

def addingnewItems(inventory, addedItems):
    for newItem in addedItems:
        inventory.setdefault(newItem, 0) #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        # inventory[newItem] =+ 1 #this is assinging the value 1 into variable inventory[newItem]
        inventory[newItem] += 1 #and this increases that value by one, each time that item appears in the loot list
    return inventory
        
    return inventory 

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inv)
print('\n --------Adding itemes-------- \n ')
for item in dragonLoot:
    print(str(item.count(item)) + " " + str(item))
addingnewItems(inv,dragonLoot)
print('\n --------New inventory after adding-------- \n ')
displayInventory(inv)