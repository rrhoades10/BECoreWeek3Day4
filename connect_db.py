import mysql.connector

def connect_db():
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

        print("Connected Succesfully")
        return conn 


    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    

