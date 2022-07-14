import os.path 
import datetime

homedir = os.path.expanduser("~")
print("Programmer", homedir)
e = datetime.datetime.now()
print("Lab 15.3", e.strftime("%b %d, %Y"), "@", e.strftime("%H:%M:%S"))

def main():
    name = input("\nEnter your name: ")
    file_name = input("Enter account to open: ")
    file_lines = []
    
    while file_name != 'charge_accounts.txt':
        print("The file could not be found")
        file_name = input("Enter account to open: ")
    readfile = open('charge_accounts.txt', 'r')
    
    for line in readfile:
        lines = line.strip()
        file_lines.append(lines)
    readfile.close()
    answer = "Y"
    while answer == "Y":
        for num in range(5):
            validate = input("Enter the account number to be validated: ")
            if validate in file_lines:
                print(f"Account number {validate} is valid")
            else:
                print(f"Account number {validate} is not valid.")

        answer = input(f"\n{name}, do you want to continue, press Y: ").upper

main()
    

        
    