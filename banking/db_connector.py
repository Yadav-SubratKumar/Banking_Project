import mysql.connector as Mycont

myDb = Mycont.connect(host="", user="", password="", database="")
db_cursor = myDb.cursor()

print("Database created --------")

# variables containing SQL queries 
insert_query = "INSERT INTO acc_details(Name,Aadhar,Age,AccNo,Pin) VALUES (%s,%s,%s,%s,%s)"
aadhar_query = "SELECT * FROM acc_details WHERE Aadhar = %s"
acc_query = "SELECT * FROM acc_details WHERE AccNo = %s"
pin_query = "SELECT * FROM acc_details WHERE Pin =  %s"
del_query = "DELETE FROM acc_details WHERE AccNo = %s"
update_query = "UPDATE acc_details SET Pin = %s WHERE Aadhar = %s;"