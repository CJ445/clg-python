inventory = {'banana': {'price': 4 , 'stock': 1 },'apple': {'price': 2, 'stock': 2},'orange': {'price':1.5, 'stock': 3 },'pear': {'price': 3, 'stock' : 4}}
for item in inventory:
    print(item)
    print(f"price: {inventory[item]['price']}")
    print(f"stock: {inventory[item]['stock']}")
    print('')

total = 0 
for item in inventory:
    indv_price = float(inventory[item]['price'])
    quantity = float(inventory[item]['stock'])
    item_worth = indv_price * quantity 
    total += item_worth
print(f"Total worth: {total}")
