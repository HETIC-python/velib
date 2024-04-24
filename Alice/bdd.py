import mariabdb

mydb = mariabdb.connect(
  host="localhost",
  user="root",
  password="",
  database="velib"
)
 
mycursor = mydb.cursor()


# Rest of sql code