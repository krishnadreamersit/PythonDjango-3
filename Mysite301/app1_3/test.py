from mydatabase import MyDatabase

mydb = MyDatabase()
# Test - Connection
# print(mydb.connect_db())

# Create table
# print(mydb.create_table())

# Insert Record
# print(mydb.insert_record(1, "Sanjaya Sharma", "Lalipur"))
# print(mydb.insert_record(2, "Bikki Goit", "Ktm"))
# print(mydb.insert_record(3, "Tripti Gurung", "Bhk"))
# print(mydb.insert_record(4, "Krishna Aryal", "Ktm"))

# Select All Records
print(mydb.select_all())

# Search Records (fullname, contactaddress)
# print(mydb.search_record('Lalipur'))

# Update Record/Edit Record
# print(mydb.update_record(1, 'Sanjaya Sharma', 'Lalitpur'))

# Delete Record
# print(mydb.delete_record(4))



