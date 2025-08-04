contacts = []

def add():
    name = input("\nNAME OF THE PERSON - ").strip().lower()
    phone_num =input("\nNUMBER OF PERSON IS - ").strip().lower()  
    email = input("\nEMIAL-ID IS - ").strip().lower()
    info = {"name":name, "phone_num":phone_num, "email":email}
    contacts.append(info)
    print(f"\nContact '{name}' added successfully!")

def view():
    if not contacts:
      print("\n----NONE----")
    else:
      for contact in contacts:
        print("\n--- CONTACT DETAILS ---")
        print("Name:", contact["name"])
        print("Phone Number:", contact["phone_num"])
        print("Email-ID:", contact["email"])

def search():
     search = input("\nTYPE NAME - ").strip().lower()
     found = False
     for contact in contacts:
      if contact["name"].lower() == search:
         print("\n----CONTACT DETAILS ARE ---- ")
         print("Name:", contact["name"])
         print("Phone:", contact["phone_num"])
         print("Email:", contact["email"])
         found = True
         break
     if not found:
         print("Contact not found.")

def update():
    updt = input("Enter the name of the contact to update: ").strip().lower()
    found = False
    for contact in contacts:
      if contact["name"].lower() == updt:
        print("NAME -", contact["name"])
        print("PHONE NUMBER -", contact["phone_num"])
        print("EMAILID -", contact["email"])

        new_phone = input("Enter new phone (or press Enter to skip): ").strip().lower()
        new_email = input("Enter new email (or press Enter to skip): ").strip().lower()

      if new_phone.strip() != "":
                contact["phone_num"] = new_phone
      if new_email.strip() != "":
                contact["email"] = new_email
                print("\nContact updated successfully!")
                found = True
                break
    if not found:
              print("Contact not found.")

def delete():
    dlt = input("Enter the name of the contact to delete: ").strip().lower()
    found = False
    for contact in contacts:
      if contact["name"].lower() == dlt:
        contacts.remove(contact)
        print("\nContact deleted successfully.")
        found = True
        break
      if not found :
           print("CONTACT NOT FOUND") 

while(True):
  print("\n WELCOME TO CONTACT BOOKS")
  print("""\n1. Add Contact  
            \n2. View Contacts  
            \n3. Search Contact  
            \n4. Update Contact  
            \n5. Delete Contact  
            \n6. Exit""")
  choice = input('ENTER YOUR CHOICE(1-6)- ')
    
  if choice == '1':
     print("\nYOU CHOSE TO ADD CONTACTS")
  elif choice == '2':
     print("\nYOU CHOSE TO VIEW CONTACTS")
  elif choice== '3':
      print("\nYOU CHOSE TO SEARCH CONTACTS")
  elif choice == '4':
       print("\nYOU CHOSE TO UPDATE CONTACTS")
  elif choice == '5':
       print("\nYOU CHOSE TO DELETE CONTACTS")
  elif choice == '6':
       print("\nEXIT")
       break
  else:
      print("\ninvalid choice")



  if choice == '1':
    add()
  elif choice == '2':
    view()
  elif choice== '3':
    search()
  elif choice == '4':
    update()
  elif choice == '5':
    delete()
  elif choice == '6':
    print("\nEXIT")
  else:
    print("\ninvalid choice")           
