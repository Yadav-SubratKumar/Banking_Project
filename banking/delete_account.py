from db_connector import *

''' Class to delete an account '''
class DeleteAccount:
    # Method to check user details
    def checkDetails(self):
        self.accountNumber = int(input("Enter your account number: "))
        self.pin = int(input("Enter your pin number: "))
      
        db_cursor.execute(acc_query, (self.accountNumber,))
        result = db_cursor.fetchone()  # Use fetchone() to retrieve a single row
        if result is None:
            print(f"^^^^^ Account Number {self.accountNumber} Not found ^^^^^")
            return False, 0
        else:
            # Checking if pin is correct or not 
            db_cursor.execute(pin_query, (self.pin,))
            result = db_cursor.fetchone()
            if result is not None:
                return True, self.accountNumber
            else:
                print("Your details are invalid, please try again")
                return False, 0

    # Method to delete Account if details are correct
    def deleteAcc(self):
        check, self.accountNumber = self.checkDetails()
        if check:
            # Actual deletion
            db_cursor.execute(del_query,(self.accountNumber,))
            myDb.commit()
            return True , self.accountNumber

        else:
            return False, 0