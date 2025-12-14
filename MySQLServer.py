import mysql.connector
from mysql.connector import Error


try :

    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        password = "Hermeses123...",
        database = "alx_book_store"
    )

    mycursor = mydb.cursor()

except Error as e:
    print(f"Error: {e}")


else:
    print(f"Database 'alx_book_store' created successfully!")

finally:
    mycursor.close()
    mydb.close()