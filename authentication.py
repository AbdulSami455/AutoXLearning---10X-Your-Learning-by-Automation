import mysql.connector

db=mysql.connector.connect(
  host="localhost",
    user="root",
    passwd="Abdullah@1234",
    database="users"
)

mycursor=db.cursor()


#created table of users with username and password as columns
#mycursor.execute("CREATE TABLE authusers(username VARCHAR(200),password VARCHAR(200))")
def signup(username, password):
    sql = "INSERT INTO authusers (username, password) VALUES (%s, %s)"
    values = (username, password)
    mycursor.execute(sql, values)
    db.commit()

