
def displayInventory(playerInventory):
    print("Inventory:")
    sum =0
    for key,value in playerInventory.items():
        print(str(value)+' '+key)
        sum +=value
    print('Total number of items: '+str(sum))

player = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)