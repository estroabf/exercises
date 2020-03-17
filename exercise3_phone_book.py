print ("Hello! I am your contact List")
print (" ")

#List of contacts
contacts = {"Estro":969179931,
            "Marco Matos": 7459617614,
            }
# User Options
while True :
    print ("If you would like to search for a contact press 1")
    print ("If you would like to add a contact to the list press 2")
    print ("If you would like to delete a contact press 3")
    print ("If you would like to see all your contacts press 4")
    print ("If you would like to modify a phone number press 5")
    print (" ")
    choice = input("What would you like to do?:").strip()
    print ("-" * 80)

# Look for a contact
    if choice == "1":
        look_contact = input("Enter the name of the contact you are looking for:").strip().title()
        print(" ")
        if look_contact in contacts:
             print (look_contact)
             print (contacts[look_contact])
             print (" ")
             print ("=" * 80)
        else:
            print("Sorry that contact cannot be found.")
            print (" ")
            print ("=" * 80)

#Add Contact n
    if choice == "2":
        add_name = input("What is the name of your new contact?:").strip().title()
        print (" ")
        
        if add_name not in contacts:
            add_phone = input("What is the phone number of your new contact?:")
            contacts[add_name] = add_phone
            print (" ")
            print ("You have now {0} in your contacts list!".format(add_name))
            print (" ")
            print ("=" * 80)

        elif add_name in contacts:
            print("You already have a contact with this name...")
            print ("-" * 60)
            print (" ")
            print ("=" * 80)

# Delete contact

    if choice == "3":
        delete_contact = input("Enter the name of the contact that you would like to delete:").strip().title()
        print (" ")

        if delete_contact not in contacts:
            print (" ")
            print ("That contact is not on the list.")
            print (" ")
            print ("=" * 80)
            
        if delete_contact in contacts:
             print (" ")
             are_u_sure = input("Are you sure that you want to delete {} from your contact list? (Y/N)".format(delete_contact)).strip().lower()
             if are_u_sure == "y":
                 del contacts [delete_contact]
                 print (" ") 
                 print ("{} has been deleted from your contacts.".format(delete_contact))
                 print (" ")
                 print ("=" * 80)

             elif are_u_sure == "n": 
                  print (" ")
                  print ("{} will not be deleted!".format(delete_contact))
                  print (" ")
                  print ("=" * 80)

        
       
#See all conntacts           
    if choice == "4":
        print (" ")
        print ("Your contact list:")
        print (contacts)
        print (" ")
        print ("=" * 80)
        
        
         
#change a number
    if choice == "5":
        print (" ")
        num_name = input("Enter the name of the contact that you would like to modify:").strip().title()
        if num_name not in contacts:
            print (" ")
            print ("Contact not on the list.")
            print (" ")
            print ("=" * 80)
        if num_name in contacts:
            print(" ")
            sure_to_modify = input("Are you sure you want to modify this number? Y/N:").strip().lower()
            if sure_to_modify == "y":
                print (" ")
                change_num = input("What is the new number?").strip()
                print (" ")
                contacts[num_name] = change_num
                print (" ")
                print ("{0} number has been changed to fuck {1}.".format(num_name, change_num))
                print (" ")
                print ("=" * 80) 

            elif sure_to_modify == "n":
                print (" ")
                print ("This contact will be unchanged.")
                print (" ")
                print ("=" * 80)

        

        
            
