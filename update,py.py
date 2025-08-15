from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.EmployeeData
def update():
   try:


       name=input("\n Enter name to update:")
       age=input("\n Enter age to been update:\n")
       country=input("\n Enter country to update:")


       (db.Employee.update_one(
           {"name":name},
           {
               "$set":{
                   "age":age,
                   "country":country
               }
           }
       ))
       print("\n Record update Successfully!!!\n")


   except Exception as e:
       print(str(e))
update()

