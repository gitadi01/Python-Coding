# Importing necessary modules and functions
from datetime import *
from operation import *
from write import *
from read import *
# Creating an empty dictionary for gadgets
gadgets = laptop_dict()
# Displaying a welcome message
Welcome()
# Initializing a loop flag
loop = True
# Getting the current date and time
Todays_date_and_time = datetime.now()
# Converting the date and time to a formatted string
dt_string = Todays_date_and_time.strftime("%Y-%m-%d %H:%M:%S")

while loop == True:
# Displaying the menu options           
    print(" ______________________________ ")
    print("|                              |")
    print("|  Enter 1 ->  TO Buy laptop.  |")
    print("|  Enter 2 ->  To Sell laptop. |")
    print("|  Enter 3 ->  To exit.        |")
    print("|______________________________|")

    print("\n")
  #asking user whether he wants to sell or order laptop or exit from the system
    input_choice = False
    while input_choice == False:
        try:        
           user_account = int(input("Hello sir. Please choose your option (1, 2 or 3): "))
           input_choice = True
        except:
            print("Invalid option. Please select again.")

    print("\n")

    if user_account == 1:
#Prompting the user for information to create an bill
        print("_______________________________________________________________")
        print("                                                               ")
        print("To create an invoice, kindly provide the required information: ")
        print("_______________________________________________________________")
        print("\n")
# Getting consumer's username and contact number        
        username = input("Please provide the consumer's username: ")
        print("\n")
        input_choice = False
        while input_choice == False:
            try:
               contactnumber = int(input("Please input the consumer's contact number: "))
               input_choice = True
            except:
                print("provide number!!")
                
            
        print("\n")

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
    # Creating an empty list to store purchased laptops
        purchased_laptop =[]
        want_more= True
    # Setting a flag to determine if the user wants to buy more laptops
        while want_more == True:
        
    # Displaying the available stock of laptops
            stock()

     # Getting the laptop ID from the user
            laptop_id=idchecker(gadgets)
      # Getting the quantity of the laptop from the user
            laptop_quantity = quantitychecker(gadgets,laptop_id)

     # Updating the stock quantity
            gadgets[laptop_id][3] = int(gadgets[laptop_id][3])-int(laptop_quantity)

        # Updating the text file with the new stock information
            textfilechange(gadgets)

    
        # Adding the purchased laptop details to the list
            product_name = gadgets[laptop_id][0]
            Brand_name = gadgets[laptop_id] [1]
            selected_quantity = laptop_quantity
            price = gadgets[laptop_id][2]
            selected_quantity_cost= gadgets[laptop_id] [2].replace("$",'')
            Total_cost = int(selected_quantity_cost)*int(selected_quantity)

            purchased_laptop.append([product_name, Brand_name, selected_quantity, price, Total_cost])
        # Asking the user if they want to buy more laptops
            laptop_demand = input("Would you like to proceed further?(Y/N)?").upper()
            Shipping_cost = 100
            Total_sum = 0
            
            if laptop_demand == "Y":
                want_more = True
            else:
          # Calculating the total cost and generating an bill
                total = 0
                for i in purchased_laptop:
                    total += int(i[4])
                Total_sum = total + Shipping_cost
            # Generating the bill with the customer's information
                Todays_date_and_time = datetime.now()
                invoiceprinting(username,contactnumber,Todays_date_and_time,purchased_laptop,Shipping_cost,Total_sum)
              
            # Printing the bill of the customer
                printbillofcustomer(username,contactnumber,Todays_date_and_time,purchased_laptop,Shipping_cost,Total_sum,dt_string)
                
    
                want_more = False


    elif user_account == 2:
        print("_______________________________________________________________")
        print("                                                               ")
        print("To create an invoice, kindly provide the required information: ")
        print("_______________________________________________________________")
        print("\n")
     # Getting customer information for the sale   
        username = input("Please provide the consumer's username: ")
        print("\n")
        

        input_choice = False
        while input_choice == False:
            try:
               contactnumber = int(input("Please input the consumer's contact number: "))
               input_choice = True
            except:
                print("provide number!!")
        print("\n")
        
        

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        # Creating an empty list to store sold laptops
        sale_laptop =[]
        sale_more= True

        while sale_more == True:
        

            stock()
            
            print("\n")

         # Getting the laptop ID from the user
            laptop_id = idchecker(gadgets)

          # Getting the quantity of the laptop to be sold
            input_choice = False
            while input_choice == False:
                try:
                    laptop_quantity = int(input("please provide the number of quantity of the laptop you want to sale:"))
                    input_choice = True
                except:
                    print("Invalid !!")
                    
            print("\n")

             # Validating the quantity
            selected_laptop_quantity = gadgets[laptop_id][3]
            while laptop_quantity <= 0 or laptop_quantity > int(selected_laptop_quantity):
                print("We regret to inform you that the desired quantity you are looking for is currently unavailable:")
                print("\n")
                input_choice = False
                while input_choice == False:
                    try:
                        laptop_quantity = int(input("Can you please specify the desired quantity of the laptop you wish to sale?:"))
                        input_choice = True
                    except:
                        print("Invalid input. Please enter a valid numeric value.")
                print("\n")

      

            # Updating the stock information in the text file

            gadgets[laptop_id][3] = int(gadgets[laptop_id][3])+int(laptop_quantity)


            textfilechange(gadgets)

    
            # Adding the sold laptop details to the list
            product_name = gadgets[laptop_id][0]
            Brand_name = gadgets[laptop_id] [1]
            selected_quantity = laptop_quantity
            price = gadgets[laptop_id][2]
            selected_quantity_cost= gadgets[laptop_id] [2].replace("$",'')
            Total_cost = int(selected_quantity_cost)*int(selected_quantity)

            sale_laptop.append([product_name, Brand_name, selected_quantity, price, Total_cost])

            # Asking the user if they want to sell more laptops

            laptop_demand = input("Would you like to proceed further?(Y/N)?").upper()
            Shipping_cost = 100
            Total_sum = 0
            
            if laptop_demand == "Y":
                sale_more = True
            else:
                # Calculating the total cost, including VAT, and generating an bill
                total = 0
                for i in sale_laptop:
                    total += int(i[4])
                    vat =total*0.13
                Total_sum = total + vat



                Todays_date_and_time = datetime.now()
                # Generating the sales order invoice with the customer's information
                Salesorderbilling(username,contactnumber,Todays_date_and_time,sale_laptop,vat,Total_sum)

        
                
        # Printing the bill of the distributor
                printbillofdistributor(username,contactnumber,Todays_date_and_time,sale_laptop,vat,Total_sum,dt_string)

                break
                more =False

    elif user_account == 3:    
                    print("\n")
                    print("___________________________________________________________________________________________")
                    print("                                                                                           ")
                    print("                       Thank you for choosing ADITYA ELECTRONIC SHOP!!                    ")
                    print("___________________________________________________________________________________________")

                    #Getting out of loop
                    within_range = True
    else:
        print("INVALID NUMBER!!. Please enter the number between (1,2,3): ")
        within_range = False
