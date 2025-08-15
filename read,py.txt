from pymongo import MongoClient


client = MongoClient('localhost:27017')
db = client.EmployeeData


def read():
   try:
       empCol = db.Employee.find()
       print("\nAll data from Employee data database\n")


       for emp in empCol:
           print(emp)


   except Exception as e:
       print(str(e))
read()
