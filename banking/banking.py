# linking the modules which are requird for the program
from create_account import CreateAccount
from delete_account import DeleteAccount
from banking_transaction import BankingTransaction
from db_connector import *

# class which inheriates all other classes and acts as central class
class Banking(CreateAccount, DeleteAccount, BankingTransaction):
    # # method to call methods of CreateAccount class
    def accountCreate(self):
        temp = self.getDetails()
        if temp != None:
            print(f"^^^^^ Your account number is: {temp} ^^^^^ ")
        else:
            print(f"^^^^^ Your pin don't match please try again ^^^^^ ")

    # method to call methods of DeleteAccount class
    def accountDelete(self):
        temp,self.accNo = self.deleteAcc()
        if temp:
            print(f"^^^^^ Your account {self.accNo} has been deleted ^^^^^")
        else:
            return 

    # method to call methods of BankingTransactions class
    def bankingTransaction(self):
        self.logIn()

print(" ||||||||||| Welcome to My Bank ||||||||||| ")


# main function which will implement the menu driven system
def main():
    print("\nHow can I help you?")
    choice = input("Choose any one:\n A - to create an account\n B - to close an existing account\n C - do banking transactions\nSelect: ")
    bank = Banking()
    if choice == 'A' or choice == 'a':
        bank.accountCreate()
    elif choice == 'B' or choice == 'b':
        bank.accountDelete()
    elif choice == 'C' or choice == 'c':
        bank.bankingTransaction()
    else:
        print("^^^^^ Please make an appropriate choice ^^^^^ ")
    # this part will call main function again if their is the user gives the appropriate input
    again = input("\nDo you want to perform more transactions? (y/n) ")
    if again == 'y':
        main()
    elif again == 'n':
        print("\n^^^^^ Thank you for using our services ^^^^^ ")
    else:
        print("\n^^^^^ Please make an appropriate choice ^^^^^ ")

if __name__ == "__main__":
    main() # calling the main function to start the code running
