# importing mysql.connector for db functionality
import mysql.connector

# setting variables with db information
# format to follow for any connection you're trying to make
# db_name = "name of your database" #ecommerce_db
# user = "your username" #root for any db instance your creating
# password = "your password"
# host = "host address"# likely 127.0.0.1 or localhost

# using our variables in our connection
# conn = mysql.connector.connect(
#     database = db_name,
#     user = user,
#     password = password,
#     host = host
# )

# doing it for realsies with our own db information
db_name = "e_commerce_db"
user = "root"
password = "Buttmuffin3!"
host = "127.0.0.1" # or 127.0.0.1

try: 
    # attempt to establish our connection
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password=password,
        host=host        
    )

    # check for a succesful connection
    if conn.is_connected():
        print(f"You have succesfully connected to {db_name}")
except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # close out the connection
    if conn and conn.is_connected():
        conn.close()
        print("MySql connection closed")


def customer_query():
    db_name = "e_commerce_db"
    user = "root"
    password = "Buttmuffin3!"
    host = "localhost" # or 127.0.0.1
    try: 
    # attempt to establish our connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password=password,
            host=host        
        )
        cursor = conn.cursor()
        # storing sql query to a variable
        query ="SELECT * FROM Customer"
        # execute the query
        cursor.execute(query)
        # fetching the results of our query
        # loops through the list of rows
        for row in cursor.fetchall():
            print(row)    
        
    except mysql.connector.Error as e:
        print(f"Error: {e}") 

    finally:
    # close out the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySql connection closed")
customer_query() # calling the function that is making our connection and running the query