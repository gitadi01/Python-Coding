def quantitychecker(gadgets, laptop_id):
    # Asks the user to input the quantity of laptops they want to purchase.
    input_choice= False
    while input_choice == False:
        try:
            laptop_quantity = int(input("Great! Now, enter the quantity of Laptop:"))
            input_choice = True
        except:
            print("Please enter a valid numeric value.")
    print("\n")

    #asks user for valid ID repeatedly;
    selected_laptop_quantity = gadgets[laptop_id][3]
    while laptop_quantity <= 0 or laptop_quantity > int(selected_laptop_quantity):
        print("We regret to inform you that the desired quantity you are looking for is currently unavailable. Kindly review the table and check if there is a different quantity that may meet your requirements.:")
        print("\n")
        input_choice = False
        while input_choice == False :
            try:
                laptop_quantity = int(input("Can you please list the desired quantity of the laptop you wish to purchase?:"))
                input_choice = True
            except:
                print("Invalid input. Please enter a valid integer")
        print("\n")
    return laptop_quantity

def idchecker(gadgets):
    input_choice = False
    while input_choice == False:
        try:
            laptop_id = int(input("Hello there! Please enter the Laptop ID:"))
            input_choice=True
        except:
            print("invalid ID")
        
    print("\n")

    #This func validates the laptopID input


    while laptop_id <= 0 or laptop_id > len(gadgets):
        print("Invalid id. Please enter a valid laptop id !!!")
        print("\n")

        input_choice = False
        while input_choice == False:
            try:
                laptop_id = int(input("Can you please specify the desired id:"))
                input_choice = True
            except:
                print("Invalid")
        
        
        
    return laptop_id
