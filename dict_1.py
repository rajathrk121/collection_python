cart = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500
}
# nameu=input("Enter item:")

# for name,price in cart.items():
#     print(name,':',price)
# for name,price in cart.items():
#     if nameu in name:
#         print("product found:",name,',','price=',price)
#     else:
#         print("Product not found")

# add_product=input("Enter product name:")
# price=int(input("Enter price:"))
# cart[add_product]=price
# print(cart)
update_price_name=input("Enter the item name you wanna to update price:")
update_price=int(input("Enter price:"))

if update_price_name in cart.keys():
    cart[update_price_name]=update_price
else:
    print('Product not found!!!')

print(cart)