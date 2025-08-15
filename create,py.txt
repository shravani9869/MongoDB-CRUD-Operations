from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData
def insert():
   try:


       employeeid = input('Enter Employee id:')
       employeeName = input('Enter name:')
       employeeAge=input('Enter Age:')
       employeeCountry = input ('Enter country:')


       db.Employee.insert_one (
           {
                "id":employeeid,
                 "name":employeeName,
               "age":employeeAge,
               "country":employeeCountry
           }
       )
       print("\nInsert Successfully\n")
   except Exception as e:


       print(str(e))


insert()
