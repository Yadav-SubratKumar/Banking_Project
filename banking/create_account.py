from db_connector import *

# Class to create an account
class CreateAccount:
    accountNumber = 0  # Static variable

    def __init__(self):
        self.accNo = CreateAccount.accountNumber + 100
    
    # Method to get details from the user
    def getDetails(self):
        self.name = input("Enter your name: ")
        self.aadharNumber = int(input("Enter your Aadhar number: "))
        self.age = int(input("Enter your age: "))
        
        CreateAccount.accountNumber += 100  # Updating static variable

        db_cursor.execute(aadhar_query, (self.aadharNumber,))
        result = db_cursor.fetchone()  # Use fetchone() to retrieve a single row
        
        if result is None:   # creating a new account and asking for pin creation
            self.pin = int(input("Enter your new pin: "))
            self.confirm = int(input("Re-enter your new pin: "))
            
            # confirming pin and updating database
            if self.confirm == self.pin:
                self.insert_values = (self.name, self.aadharNumber, self.age, self.accNo+self.pin, self.pin)
                db_cursor.execute(insert_query, self.insert_values)
                myDb.commit()
                return self.accNo+self.pin
        else:
            print(f"^^^^^ Aadhar Number {self.aadharNumber} already has an account ^^^^^")