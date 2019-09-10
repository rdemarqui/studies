#Fantasy Game, page 161

def displayInventory(self):
    print('Invetory:')
    total = 0
    for k, v in self.items():
        print(v , k)
        total = total + v
    print('Total number of items:', total)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1

wizard = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(wizard, dragonLoot)

displayInventory(wizard)
