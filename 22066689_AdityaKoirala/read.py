def laptop_dict():
    # Reads the contents of the "laptop.txt" file
    file = open ("laptop.txt", "r")

    gadgets = {}
    gadgets_id = 1
    for line in file:
        line = line.replace("\n","")
        gadgets.update({gadgets_id: line.split(",")})
        gadgets_id = gadgets_id + 1
    file.close()
    return gadgets



def stock():
    #Displays the stock of laptops available.
    print("______________________________________________________________________________________________________________________________")
    print("                                                                                                                              ")
    print("S.N. \t\tLaptop Name     Brand Name\tprice\t       quantity\t       Processor\tGraphics Card")
    print("______________________________________________________________________________________________________________________________")
   #reads the "laptop.txt" file and prints the details of each laptop.
    file = open("laptop.txt", "r")
    a = 1
    for line in file:
        print(a, "\t\t"+line.replace(",", "\t\t"))
        a = a+1
    print("-----------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")
