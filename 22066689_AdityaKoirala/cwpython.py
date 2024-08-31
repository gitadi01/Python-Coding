
from datetime import datetime
#this func will show initial message

def Welcome():
    print("\n")
    print("***************************************************************")
    print("*                                                             *")
    print("*         WELCOME TO ADITYA ELECTRONIC SHOP                   *")
    print("*                                                             *")
    print("***************************************************************")

    
def printbillofcustomer(username,contactnumber,Todays_date_and_time,purchased_laptop,Shipping_cost,Total_sum,dt_string):
    file= open(str(username)+str(contactnumber)+".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t ADITYA ELECTRONIC SHOP bill")
    file.write("\n")
    file.write("\t \t Kalanki, Kathmandu | Contact Number:9812540634 \n")
    file.write("\n")
    file.write("-------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("CUSTOMER INFORMATION:")
    file.write("\n")
    file.write("-------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Name of the costumer:"+str(username)+"\n")
    file.write("\n")
    file.write("contact number: "+str(contactnumber)+"\n")
    file.write("\n")
    file.write("Date and Time of purchase: "+str(Todays_date_and_time)+"\n")
    file.write("\n")
    file.write("-------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("PURCHASE DETAILS:")
    file.write("\n")
    file.write("_____________________________________________________________________________________")

    file.write("\n")
    file.write("Item Name  \tBrand Name  \tTotal Quantity \t \t Unit price   \t\tTotal")
    file.write("\n")
    file.write("_____________________________________________________________________________________")

    file.write("\n")
    for i in purchased_laptop:
        file.write(str(i[0]) + '\t\t' + str(i[1]) + '\t\t' + str(i[2]) + '\t\t\t '  + str(i[3])+'\t\t\t' + str(i[4]) +"\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("your Shipping cost is:$"+""+str(Shipping_cost)+"\n")
    file.write("Total_sum: $"+str(Total_sum)+"\n")
    file.write("\n")
    file.write("\t!!!!!!!!!Thank you for choosing our shop for your recent purchase!!!!!!!!!!!!!"+"\n")
    file.write("\n")
    print("--------------------------------------------------------------------------------------")
    file.close()

def printbillofdistributor(username,contactnumber,Todays_date_and_time,sale_laptop,vat,Total_sum,dt_string):
    file= open(str(username)+str(contactnumber)+".txt", "w")
    file.write("\n")
    file.write("\t \t \t \t ADITYA ELECTRONIC SHOP bill")
    file.write("\n")
    file.write("\t \t Kalanki, Kathmandu | Contact Number:9812540634 \n")
    file.write("\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("CUSTOMER INFORMATION:")
    file.write("\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("Name of the costumer:"+str(username)+"\n")
    file.write("\n")
    file.write("contact number: "+str(contactnumber)+"\n")
    file.write("\n")
    file.write("Date and Time of sale: "+str(Todays_date_and_time)+"\n")
    file.write("\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("SALES DETAILS:")
    file.write("\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("Item Name  \tBrand Name  \tTotal Quantity \t \t Unit price   \t\tTotal")
    file.write("\n")
    file.write("_____________________________________________________________________________________")

    file.write("\n")
    for i in sale_laptop:
        file.write(str(i[0]) + '\t\t' + str(i[1]) + '\t\t' + str(i[2]) + '\t\t\t '  + str(i[3])+'\t\t\t' + str(i[4]) +"\n")
    file.write("_____________________________________________________________________________________")
    file.write("\n")
    file.write("vat cost is:$"+""+str(vat)+"\n")
    file.write("Total_sum: $"+str(Total_sum)+"\n")
    file.write("\n")
    file.write("\t\t\t!!!!!!!!!Thankyou Visit Again!!!!!!!!!!!!"+"\n")
    file.write("\n")
    print("--------------------------------------------------------------------------------------")
    file.close()



file = open ("laptop.txt", "r")

gadgets = {}
gadgets_id = 1
for line in file:
    line = line.replace("\n","")
    gadgets.update({gadgets_id: line.split(",")})
    gadgets_id = gadgets_id + 1
file.close()
Welcome()
loop = True
Todays_date_and_time = datetime.now()

dt_string = Todays_date_and_time.strftime("%Y-%m-%d %H:%M:%S")
while loop == True:
           
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
        print("_______________________________________________________________")
        print("                                                               ")
        print("To create an invoice, kindly provide the required information: ")
        print("_______________________________________________________________")
        print("\n")
        try:
            username = (input("Please provide the consumer's username: "))
        except:
            print("provide user name!!")
            username =(input("Please provide the consumer's username: "))
            
        print("\n")
        print("\n")
        try:
            contactnumber = int(input("Please input the consumer's contact number: "))
        except:
            print("provide number!!")
            contactnumber = int(input("Please input the consumer's contact number: "))
            
        print("\n")

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        purchased_laptop =[]
        want_more= True

        while want_more == True:
        

            print("______________________________________________________________________________________________________________________________")
            print("                                                                                                                              ")
            print("S.N. \t\tLaptop Name     Brand Name\tprice\t       quantity\t       Processor\tGraphics Card")
            print("______________________________________________________________________________________________________________________________")


            file = open("laptop.txt", "r")
            a = 1
            for line in file:
                print(a, "\t\t"+line.replace(",", "\t\t"))
                a = a+1
            print("-----------------------------------------------------------------------------------------------------------------------------")
            file.close()
            print("\n")

            #user id
            try:
                laptop_id = int(input("Hello there! Please enter the Laptop ID:"))
            except:
                print("invalid ID")
                laptop_id = int(input("Hello there! Please enter the Laptop ID:"))
                
            print("\n")

            #This func validates the laptopID input
       

            while laptop_id <= 0 or laptop_id > len(gadgets):
                print("Invalid id. Please enter a valid laptop id !!!")
                print("\n")

                laptop_id = int(input("Can you please specify the desired quantity of the laptop you wish to purchase?:"))

            #laptop quantity
            try:
                laptop_quantity = int(input("Great! Now, enter the quantity of Laptop:"))
            except:
                print("Enter quantity of Laptop!!")
                laptop_quantity = int(input("Great! Now, enter the quantity of Laptop:"))
                
            print("\n")

            #asks user for valid ID repeatedly;
            selected_laptop_quantity = gadgets[laptop_id][3]
            while laptop_quantity <= 0 or laptop_quantity > int(selected_laptop_quantity):
                print("We regret to inform you that the desired quantity you are looking for is currently unavailable. Kindly review the table and check if there is a different quantity that may meet your requirements.:")
                print("\n")

                laptop_quantity = int(input("Can you please specify the desired quantity of the laptop you wish to purchase?:"))
                print("\n")

      

            #coverting items inside list into string type
        

            gadgets[laptop_id][3] = int(gadgets[laptop_id][3])-int(laptop_quantity)


            file = open("laptop.txt", "w")

            for values in gadgets.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

    
            #Following block of code enables to purchase laptop
            product_name = gadgets[laptop_id][0]
            Brand_name = gadgets[laptop_id] [1]
            selected_quantity = laptop_quantity
            price = gadgets[laptop_id][2]
            selected_quantity_cost= gadgets[laptop_id] [2].replace("$",'')
            Total_cost = int(selected_quantity_cost)*int(selected_quantity)

            purchased_laptop.append([product_name, Brand_name, selected_quantity, price, Total_cost])

            laptop_demand = input("Would you like to proceed further?(Y/N)?").upper()
            Shipping_cost = 100
            Total_sum = 0
            
            if laptop_demand == "Y":
                want_more = True
            else:
                total = 0
                for i in purchased_laptop:
                    total += int(i[4])
                Total_sum = total + Shipping_cost



                Todays_date_and_time = datetime.now()
                print("\n")
                print("`````````````````````````````````````````````````````````````````````````````````````")
                print("\t \t \t \t ADITYA ELECTRONIC SHOP bill                                              ")
                print("                                                                                     ")
                print("\t \t Kalanki, Kathmandu | Contact Number:9812540634                                 ")
                print("                                                                                     ")
                print("`````````````````````````````````````````````````````````````````````````````````````")
                print("\n")
                print("_____________________________________________________________________________________")
                print("                                                                                     ")
                print("CUSTOMER INFORMATION:")
                print("_____________________________________________________________________________________")
                print("                                                                                     ")
                print("Name of the costumer:"+str(username))
                print("-------------------------------------------------------------------------------------")
                print("contact number: "+str(contactnumber))
                print("-------------------------------------------------------------------------------------")
                print("Date and Time of purchase: "+str(Todays_date_and_time),)
                print("-------------------------------------------------------------------------------------")
                print("\n")
                print("_____________________________________________________________________________________")
                print("                                                                                     ")
                print("PURCHASE DETAILS:")
                print("_____________________________________________________________________________________")
                print("                                                                                     ")
                print("Item Name  \tBrand Name  \tTotal Quantity \t \t Unit price   \t\tTotal")
                print("_____________________________________________________________________________________")

                for i in purchased_laptop:
                    print(str(i[0]) + '\t\t' + str(i[1]) + '\t\t' + str(i[2]) + '\t\t\t '  + str(i[3])+'\t\t\t' + str(i[4]) +"\n")

                print("_____________________________________________________________________________________")
                print("\n")
                print('Shipping cost is: $' + str(Shipping_cost) + '\n')
                print('Total_sum: $' + str(Total_sum) + '\n')
                print("\n")
                print("\t!!!!!!Thank you for choosing our shop for your recent purchase!!!!!!!!!!"+"\n")
                print("\n")
              
                  
            

           
            
                file= open(str(username)+str(contactnumber)+".txt", "w")
                file.write("\n")
                file.write("\t \t \t \t ADITYA ELECTRONIC SHOP bill")
                file.write("\n")
                file.write("\t \t Kalanki, Kathmandu | Contact Number:9812540634 \n")
                file.write("\n")
                file.write("______________________________________________________________________________________")
                file.write("                                                                                      ")
                file.write("\n")
                file.write("CUSTOMER INFORMATION:")
                file.write("\n")
                file.write("______________________________________________________________________________________")
                file.write("\n")
                file.write("Name of the costumer:"+str(username)+"\n")
                file.write("\n")
                file.write("contact number: "+str(contactnumber)+"\n")
                file.write("\n")
                file.write("Date and Time of purchase: "+str(Todays_date_and_time)+"\n")
                file.write("\n")
                file.write("_____________________________________________________________________________________")
                file.write("\n")
                file.write("PURCHASE DETAILS:")
                file.write("\n")
                file.write("_____________________________________________________________________________________")
                file.write("                                                                                     ")
                file.write("\n")
                file.write("Item Name \t \t Brand Name   \tTotal Quantity \t \t Unit price \t\t\tTotal")
                file.write("\n")
                file.write("_____________________________________________________________________________________")

                file.write("\n")
                for i in purchased_laptop:
                    file.write(str(i[0])+"\t\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t\t"+str(i[3])+str(i[4])+"\t\t")
                file.write("-------------------------------------------------------------------------------------")
                file.write("\n")
                file.write("your Shipping cost is:$"+""+str(Shipping_cost)+"\n")
                file.write("Total_sum: $"+str(Total_sum)+"\n")
                file.write("\n")
                file.write("\t!!!!!!!!!Thank you for choosing our shop for your recent purchase!!!!!!!!!!!!!"+"\n")
                file.write("\n")
                print("--------------------------------------------------------------------------------------")
                file.close()
                printbillofcustomer(username,contactnumber,Todays_date_and_time,purchased_laptop,Shipping_cost,Total_sum,dt_string) 
    
                want_more = False


    elif user_account == 2:
        print("_______________________________________________________________")
        print("                                                               ")
        print("To create an invoice, kindly provide the required information: ")
        print("_______________________________________________________________")
        print("\n")
        try:
           username = input("Please provide the consumer's username: ")
        except:
            print("Provide user name!!")
            username = input("Please provide the consumer's username: ")
        print("\n")
        try:
           contactnumber = int(input("Please input the consumer's contact number: "))
        except:
            print("provide number!!")
            contactnumber = int(input("Please input the consumer's contact number: "))
        print("\n")

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

        sale_laptop =[]
        sale_more= True

        while sale_more == True:
        

            print("______________________________________________________________________________________________________________________________")
            print("                                                                                                                              ")
            print("S.N. \t\tLaptop Name     Brand Name\tprice\t       quantity\t       Processor\tGraphics Card")
            print("______________________________________________________________________________________________________________________________")

            file = open("laptop.txt", "r")
            a = 1
            for line in file:
                print(a, "\t\t"+line.replace(",", "\t\t"))
                a = a+1
                
            print("-----------------------------------------------------------------------------------------------------------------------------")
            file.close()
            print("\n")

            #user id
            try:
                laptop_id = int(input("Hello there! Please enter the Laptop ID you want to Sale:"))
            except:
                print("Invalid ID")
                laptop_id = int(input("Hello there! Please enter the Laptop ID you want to Sale:"))
            print("\n")

            #valid id

            while laptop_id <= 0 or laptop_id > len(gadgets):
                print("Invalid id. Please enter a valid laptop id !!!")
                print("\n")

                laptop_id = int(input("Can you please specify the desired quantity of the laptop you wish to sale?:"))

            #laptop quantity
            try:
               laptop_quantity = int(input("please provide the number of quantity of the laptop you want to sale:"))
            except:
                print("Invalid ID!!")
                laptop_quantity = int(input("please provide the number of quantity of the laptop you want to sale:"))
                
            print("\n")

            #valid quantity
            selected_laptop_quantity = gadgets[laptop_id][3]
            while laptop_quantity <= 0 or laptop_quantity > int(selected_laptop_quantity):
                print("We regret to inform you that the desired quantity you are looking for is currently unavailable. Kindly review the table and check if there is a different quantity that may meet your requirements.:")
                print("\n")

                laptop_quantity = int(input("Can you please specify the desired quantity of the laptop you wish to sale?:"))
                print("\n")

      

            #update the text file

            gadgets[laptop_id][3] = int(gadgets[laptop_id][3])+int(laptop_quantity)


            file = open("laptop.txt", "w")

            for values in gadgets.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

    
            #sold
            product_name = gadgets[laptop_id][0]
            Brand_name = gadgets[laptop_id] [1]
            selected_quantity = laptop_quantity
            price = gadgets[laptop_id][2]
            selected_quantity_cost= gadgets[laptop_id] [2].replace("$",'')
            Total_cost = int(selected_quantity_cost)*int(selected_quantity)

            sale_laptop.append([product_name, Brand_name, selected_quantity, price, Total_cost])

            laptop_demand = input("Would you like to proceed further?(Y/N)?").upper()
            Shipping_cost = 100
            Total_sum = 0
            
            if laptop_demand == "Y":
                sale_more = True
            else:
                total = 0
                for i in sale_laptop:
                    total += int(i[4])
                    vat =total*0.13
                Total_sum = total + vat



                Todays_date_and_time = datetime.now()
                print("\n")
                print("\t \t \t \t ADITYA ELECTRONIC SHOP bill")
                print("\n")
                print("\t \t Kalanki, Kathmandu | Contact Number:9812540634 ")
                print("\n")
                print("-------------------------------------------------------------------------------------")
                print("CUSTOMER INFORMATION:")
                print("-------------------------------------------------------------------------------------")
                print("Name of the costumer:"+str(username))
                print("contact number: "+str(contactnumber))
                print("Date and Time of purchase: "+str(Todays_date_and_time),)
                print("-------------------------------------------------------------------------------------")
                print("\n")
                print("SALES DETAILS:")
                print("_____________________________________________________________________________________")
                print("                                                                                     ")
                print("Item Name  \tBrand Name  \tTotal Quantity \t \t Unit price   \t\tTotal")
                print("_____________________________________________________________________________________")
                for i in sale_laptop:
                     print(str(i[0]) + '\t\t' + str(i[1]) + '\t\t' + str(i[2]) + '\t\t\t '  + str(i[3])+'\t\t\t' + str(i[4]) +"\n")
                

                print("-------------------------------------------------------------------------------------")
                print("\n")
            
           
                print("vat cost is :$" +"" +str(vat) + "\n")
            
          

           
                print('Total_sum: $' + str(Total_sum) + '\n')

                print("\n")
                print("\t\t\t!!!!!!*Thankyou Visit Again*!!!!!!!!!"+"\n")
                print("\n")
                print("--------------------------------------------------------------------------------------")

                           
                
                
                
                #Todays_date_and_time = datetime.now()

                printbillofdistributor(username,contactnumber,Todays_date_and_time,sale_laptop,vat,Total_sum,dt_string)

                break
                more =False

    elif user_account == 3:    
                    print("\n")
                    print("___________________________________________________________________________________________")
                    print("                                                                                           ")
                    print("                       Thank you for choosing ADITYA ELECTRONIC SHOP !!                    ")
                    print("___________________________________________________________________________________________")

                    #Getting out of loop
                    within_range = True
    else:
        print("INVALID NUMBER!!. Please enter the number between (1,2,3): ")
        within_range = False
        
                
            

           


     
            
                
                
            
            
            
            
           
            
                   
                    
            
            
            
    

            
            

        
        
  
            
            
