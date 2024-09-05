from datetime import datetime

def welcome_message():
    print("\n")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("\t \t   Welcome to our system. I hope you have a good time here")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("\n")
    
def read_txt():
    with open("equipment.txt",'r') as file:
        myDictionary = {}
        itemSN=1
        for line in file:
            line=line.replace("\n","")
            myDictionary[itemSN]= line.split(",")

            itemSN= itemSN+1
        file.close()
        return myDictionary
    
def bill_1():
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("You must enter your personal info for billing purposes.  ")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    name = input("Please enter your Full Name: ")
    number = input("Please enter your Phone Number: ")
    return name,number

def display_equipments():
    print("\t\t\t~~~~~~Equipment DETAILS~~~~~~~\t\t\t")
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    print("S.N. \t Equipments Name \t \t \t Brand \t \t \t Price \t \t Quantity")
    s = 1
    file = open("equipment.txt","r")
    for line in file:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print(s,"\t"+line.replace(",","\t"))
        s+=1
    file.close()

def valid_sn1():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    valid_sn = int(input("Please provide the SN of the item you want to rent: "))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    return valid_sn

def valid_sn2():
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    valid_snn = int(input("Please provide the SN of the item you want to return: "))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    return valid_snn

def display_opt():
    print("Here are some available options: ")
    print("---------------------------------------------------")
    print("\t Press 1 to rent an equipment")
    print("\t Press 2 to return")
    print("\t Press 3 to exit")
    print("---------------------------------------------------")
    userinput=int(input("Please select an option: "))
    return userinput