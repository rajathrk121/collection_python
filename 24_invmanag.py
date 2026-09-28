inventory = {
"Laptop": {"price": 50000, "quantity": 5},
"Mouse": {"price": 500, "quantity": 20},
"Keyboard": {"price": 1500, "quantity": 10}
}

# print(inventory)

sum=0
for pri , quan in inventory.items():
    product= quan["price"]*quan["quantity"]
    sum+=product


for pri , quan in inventory.items():
    if quan['quantity']<10:
        print(inventory[pri])
print(sum)

inventory["Keyboard"]['quantity']=20
inventory["Mic"]={
    "price":1500,"quantity":25
}
inventory.pop("Keyboard")

print(inventory)
