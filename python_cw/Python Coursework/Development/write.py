from operation import *

def write_rent(name,phone,today_date_and_time,user_purchased_equipments,grand_total):
    print("\n")
    print("---------------------------------------------------------------------------------------------------------")
    with open(name+phone+".txt","w") as file:
        file.write("\n")
        file.write("\t \t \t \t   Sikum's Equipment Rental shop")
        file.write("\n")
        file.write("\t \t \t \t Kamalpokhari, Kathmandu | Contact No: 9855854555")
        file.write("\n")
        file.write("---------------------------------------------------------------------------------------------------------")
        file.write("Equipment Details are:")
        file.write("--------------------------------------------------------------------------------------")
        file.write("Name of the Costumer:"+str(name) +"\n")
        file.write("Contact number: "+str(phone)+"\n")
        file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
        file.write("---------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Purchase Detail are:")
        file.write("--------------------------------------------------------------------------------------")
        file.write("Equioment Name \t\t Total Quantity \t\t Unit Price \t\tTotal")
        file.write("--------------------------------------------------------------------------------------------")
        for i in user_purchased_equipments:
            file.write(str(i[0])+"\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t"+"$"+str(i[3])+"\n")
            file.write("---------------------------------------------------------------------------------------------------------")

        file.write("Grand Total: $"+str(grand_total))
        file.write("Note: Fine cost will added to the grand total in case of delay")
            
def write_return(name,phone,today_date_and_time,user_returned_equipments,grand_total):
    print("\n")
    print("---------------------------------------------------------------------------")
    with open(name+phone+".txt","w") as file:
        file.write("\n")
        file.write("\t \t \t \t   Sikum's Equipment Rental shop")
        file.write("\n")
        file.write("\t \t \t \t Kamalpokhari, Kathmandu | Contact No: 9855854555")
        file.write("\n")
        file.write("---------------------------------------------------------------------------------------------------------")
        file.write("Equipment Details are:")
        file.write("---------------------------------------------------------------------------")
        file.write("Name of the Costumer:"+str(name)+"\n")
        file.write("Contact number: "+str(phone)+"\n")
        file.write("Date and time of purchase: "+str(today_date_and_time)+"\n")
        file.write("---------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Purchase Detail are:")
        file.write("---------------------------------------------------------------------------")
        file.write("Equipments Name \t\t Total Quantity \t\t Unit Price \t\t\tTotal")
        file.write("---------------------------------------------------------------------------------------------------------")
        for i in user_returned_equipments:
            file.write(str(i[0])+"\t\t"+str(i[1])+"\t\t\t"+str(i[2])+"\t\t"+"$"+str(i[3])+"\n")
            file.write("---------------------------------------------------------------------------------------------------------")

        #file.write("Fine: $"+str(fine))
        file.write("Grant Total: $"+str(grand_total))
        
        
    
