from db_connector import *
from delete_account import DeleteAccount
# Class to perform other transactions
class BankingTransaction():
    # method to create a prompt to allow user to perform other banking operations
    def prompt(self):
        self.choice = input("What can we do for you?\n A - Change pin\n B - Loan\n C - F.D\n Select: ")
        if self.choice == "A" or self.choice == "a":
            self.changePin()

        elif self.choice == "B" or self.choice == "b":
            print("You can get a loan right now.")
        elif self.choice == "C" or self.choice == "c":
            print("You can get an FD service.")
    # method to confirm the user login details
    def logIn(self):
        self.temp, self.accountNumber = DeleteAccount().checkDetails()
        if self.temp:
            self.prompt()
    # method to change the pin number of account holder
    def changePin(self):
        # checking if the user is a account holder or not 
        self.aadharNo = int(input("Enter your Aadhar number: "))
        db_cursor.execute(aadhar_query,(self.aadharNo,))
        result = db_cursor.fetchone()
        # process of changing the pin
        if result:
            self.pin = int(input("Enter your new pin: "))
            self.confirm = int(input("Re-enter your new pin: "))
            if self.pin == self.confirm:
                db_cursor.execute(update_query,(self.pin,self.aadharNo))
                myDb.commit()
            else:
                print("^^^^^ Re-entered pin does not matches to new pin ^^^^^")
        else:
            print(f"^^^^^ Aadhar Number {self.aadharNumber} does not have an account ^^^^^")
            return

        print("You just changed your pin.")
