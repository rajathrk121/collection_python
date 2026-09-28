product={
    "phone":35000,
    "phone case": 150,
    "screen guard":150
}

product["heaphone"]=150

product['phone']=5000

del product["screen guard"]

print(product)

search="headphone"

if search in product:
    print("Product found")
else:
    print("Product not found")


for i in product:
    if product[i]>500:
        print(product[i],i)