#displays a welcome message to the user
def Welcome():
    print("\n")
    print("***************************************************************")
    print("*                                                             *")
    print("*         WELCOME TO ADITYA ELECTRONIC SHOP                   *")
    print("*                                                             *")
    print("***************************************************************")
    
def textfilechange(gadgets):
    file = open("laptop.txt", "w")

    for values in gadgets.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()
#prints the invoice 
def invoiceprinting(username,contactnumber,Todays_date_and_time,purchased_laptop,Shipping_cost,Total_sum):
    print("\n")
    print("`````````````````````````````````````````````````````````````````````````````````````")
    print("\t \t \t \t ADITYA ELECTRONIC SHOP bill                                                      ")
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
    print("Name of the customer:"+str(username))
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

def Salesorderbilling(username,contactnumber,Todays_date_and_time,sale_laptop,vat,Total_sum):
    print("\n")
    print("\t \t \t \t ADITYA ELECTRONIC SHOP bill")
    print("\n")
    print("\t \t Kalanki, Kathmandu | Contact Number:9812540634 ")
    print("\n")
    print("-------------------------------------------------------------------------------------")
    print("CUSTOMER INFORMATION:")
    print("-------------------------------------------------------------------------------------")
    print("Name of the customer:"+str(username))
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
#prints the bill of the customer
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
    file.write("Name of the customer:"+str(username)+"\n")
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
# prints the bill of the distributor
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
    file.write("Name of the customer:"+str(username)+"\n")
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
