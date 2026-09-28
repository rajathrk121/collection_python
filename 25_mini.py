print("1.Add Contact \n2.View Contact \n3.Search Contact \n4.Update Contact \n5.Delete Contact \n6 exit")

choice = int(input("Enter your choice: "))

contact={
    
}
match choice:
    case 1:
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        email=input("Enter email address: ")

        contact={name:{'phone number':phone,'email_id':email}}

        print("Contact added successfully")
        print(contact)
    case 2:
        print(contact)
    case 3:
        s_name=input("Enter name: ")
        if s_name in contact:
            print (contact[s_name])
        else:
            print("contact not found!!!")
    case 4:
        print("1. Update name \n2. Update phone number \n3. Update emailaddress")
        choice = int(input("Enter your choice: "))
        if choice ==1:
            u_name=input("Enter name: ")
            contact['name']=u_name



