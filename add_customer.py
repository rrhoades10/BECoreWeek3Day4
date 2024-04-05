import mysql.connector

def add_customer():
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
        cursor = conn.cursor()
        name = input("Who woud you like to enter into your database? ")
        email = input("What is their email? ")
        phone = input("What is their phone number? ")
        # customer to be added in a tuple
        new_customer = (name, email, phone)

        # sql query to add our customer
        query = "INSERT INTO Customer (name, email, phone) VALUES (%s, %s, %s)"

        # execute query with new customer
        cursor.execute(query, new_customer)
        conn.commit()
        print("New Customer was succesfully added")


    
    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # close out the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySql connection closed")

add_customer()
