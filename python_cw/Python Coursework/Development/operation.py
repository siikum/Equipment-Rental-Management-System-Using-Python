from datetime import datetime
from read import *
from write import *

def rent_function():
    myDictionary = read_txt() 
    user_purchased_equipments = []
    
    while True:
        display_equipments()
        valid_sn = valid_sn1()
        # Valid ID
        while valid_sn <=0 or valid_sn > len(myDictionary):         #
            print("Invalid Entry.Please provide a valid equipment ID !!!")
            print("\n")
            valid_sn = int(input("Please enter S.N. of the Equipment you want to rent: "))
            
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        user_quantity = int(input("Please provide the number of quantity of the equipment you want to rent: "))
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

        #Valid quantity
        get_quantity_of_selected_equipment = myDictionary[valid_sn][3]    
        while user_quantity <=0 or user_quantity > int(get_quantity_of_selected_equipment):
            print("Dear Admin, the Equipment you are looking for is not available at the moment. Please check the table and insert the Equipmwnt")
            print("\n")

            try:
                user_quantity = int(input("Please provide a valid positive quantity: "))
            except ValueError:
                print("Please enter a valid integer value.")
                continue
            print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

        #Update the text file

        myDictionary[valid_sn][3] = int(myDictionary[valid_sn][3]) -int(user_quantity)
        file = open("equipment.txt","w")

        for values in myDictionary.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()

        # getting user purchased equipments

        name_of_product = myDictionary[valid_sn][0]
        quantity_selected_by_user = user_quantity
        unit_price = myDictionary[valid_sn][2]
        price_of_selected_equipment = myDictionary[valid_sn][2].replace("$",'')
        total_price = int(price_of_selected_equipment)*int(quantity_selected_by_user)

        user_purchased_equipments.append([name_of_product, quantity_selected_by_user, unit_price,total_price])

        # Ask the user if they want to continue selecting 
        user_req = input("Dear user do you want to rent any more equipment? If yes press, 'Y' else press 'N' to exit: ").upper()
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("\n")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

        if user_req.lower()=='n':
            break
        elif user_req.lower() !="y":
            continue

    total = 0
            
    for i in user_purchased_equipments:
        total+=int(i[3])
    grand_total = total
    today_date_and_time = datetime.now()
    name,phone = bill_1()
    print("\n")
    print("\t \t \t \t   Sikum's Equipment shop")
    print("\n")
    print("\t \t \t \t   Kamalpokhari, Kathmandu | Contact No: 9855854555")
    print("\n")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Equipment Details are:")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Name of the Costumer:"+str(name))
    print("Contact number: "+str(phone))
    print("Date and time of purchase: "+str(today_date_and_time))
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("\n")
    print("Purchase Detail are:")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Equipments Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    for i in user_purchased_equipments:
        print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t","$",i[3])
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

    print("Grand Total: $"+str(grand_total))
    print("Note: Fine cost will added to the grand total in case of late return")

    write_rent(name,phone,today_date_and_time,user_purchased_equipments,grand_total)

def return_function():
    myDictionary = read_txt() 
    user_returned_equipments = []
    fine = 0
    fineday=0
    more= True
    while more==True:
        display_equipments()
        valid_snn = valid_sn2()

        # Valid ID
        while valid_snn <=0 or valid_snn > len(myDictionary):         #
            print("Invalid Entry.Please provide a valid equipment's S.N. !!!")
            print("\n")
            valid_snn = int(input("Please provide the S.N. of the equipment you want to return: "))
            
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        user_quantity = int(input("Please provide the number of quantity of the equipment you want to return: "))
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

        #Valid quantity

        get_quantity_of_selected_equipment = myDictionary[valid_snn][3]    
        while user_quantity <=0 or user_quantity > int(get_quantity_of_selected_equipment):
            print("Dear Admin, the equipment you are looking for is not available at the moment. Please check the table and insert the equipment")
            print("\n")
            try:
                user_quantity = int(input("Please provide a valid positive quantity: "))
            except ValueError:
                print("Please enter a valid integer value.")
                continue
            print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")

        #Update the text file
        myDictionary[valid_snn][3] = int(myDictionary[valid_snn][3])+ int(user_quantity)
        file = open("equipment.txt","w")

        for values in myDictionary.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
            file.write("\n")
        file.close()
        # getting user purchased equipments

        name_of_product = myDictionary[valid_snn][0]
        quantity_selected_by_user = user_quantity
        unit_price = myDictionary[valid_snn][2]
        price_of_selected_equipment = myDictionary[valid_snn][2].replace("$",'')
        total_price = int(price_of_selected_equipment)*int(quantity_selected_by_user)
        try:
            rentDays=int(input("Enter the number of days you were late: "))
            if rentDays<1:
                print("Invalid rented Days.Please Enter Again.") #print statem t 
            else:
                if rentDays<=5:
                    fine=0
                elif rentDays%5 !=0:
                    fineday=(int(rentDays//5)+1)
                    fine=int((fineday/5))*int(price_of_selected_equipment)
                else:
                    fine=(rentDays-5)*int(price_of_selected_equipment)

                anss= input("Dear user do you want to return any more equipment? If yes press, 'Y' else press 'Enter' key.").upper()

                if anss=="Y":
                    print("\n")
                    more=True
                else:
                    more=False

                grand_total=0
                if anss=="Y":
                    more=True
                else:
                    total=0
                    for i in user_returned_equipments:
                        total=total+int(i[3])
                    grand_total= total+fine
                    today_date_and_time = datetime.now()
                #break
        except ValueError:
            print("Invalid days.Please try Again")
            print("\n")

        user_returned_equipments.append([name_of_product, quantity_selected_by_user, unit_price,total_price ,rentDays,fine])
        # Ask the user if they want to continue selecting 
        print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
        print("\n")
        

    total = 0
    for i in user_returned_equipments:
        total+=int(i[3])
    grand_total = total
    today_date_and_time = datetime.now()
    name,phone = bill_1()
    print("\n")
    print("\t \t \t \t   Sikum's Equipment Rental shop")
    print("\n")
    print("\t \t \t \t Kamalpokhari, Kathmandu | Contact No: 9855854555")
    print("\n")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Equipment Details are:")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Name of the Costumer:"+str(name))
    print("Contact number: "+str(phone))
    print("Date and time of purchase: "+str(today_date_and_time))
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("\n")
    print("Purchase Detail are:")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Equioment Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    for i in user_returned_equipments:
        print(i[0],"\t\t",i[1],"\t\t",i[2],"\t\t","$",i[3])
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("Fine: $"+str(fine))
    print("Grand Total: $"+str(grand_total))

    write_return(name,phone,today_date_and_time,user_returned_equipments,grand_total)