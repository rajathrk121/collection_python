inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

print(inventory)
while True:
    print("1 for search item \n2 for add stock \n3 for sell product \n4 for exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            search_item = input("Enter item name: ")
            if search_item in inventory:
                print(inventory[search_item])
            else:
                print("Product not exist")

        case 2:
            Add_stock=input("Enter stock name: ")
            quantity=int(input("Enter item quantity: "))
            
            if Add_stock in inventory:
                inventory[Add_stock]+=quantity
                print("Updateds quantity: ",inventory[Add_stock])
            else:
                print("Enter a valid product!!!")

        case 3:
            name=input("Enter product name: ")
            
            sell_quantity=int(input("Enter sell quantity: "))
            
            if name in inventory:
                if sell_quantity <= inventory[name]:
                    inventory[name]-=sell_quantity
                    print("Updated stock:", inventory[name])
            
                else:
                    print("Enough stock not in the store")
            
            else:
                print("Enter a valid product name!!!")

        case 4:
            exit()

        case _:
            print('Enter a valid choice!!!')