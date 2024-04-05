from connect_db import connect_db

def update_customer():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # variable for the updated customer
            # always looking for a tuple - when data is involved
            updated_customer = ("Mace Windu", 4)

            # query
            # %s is assigned positionally based on the updated_customer variable
            # cursor.excute is expecting an iterable to grab positionally whats inside
            query = "UPDATE Customer SET name = %s WHERE customer_id = %s"

            # Executing the query
            cursor.execute(query, updated_customer)
            conn.commit() # because we're changing data
            print("Customer details succesfully updated!")

        except Exception as e:
            print(f"and error occurred: {e}") 
        
        finally:
            cursor.close()
            conn.close()
update_customer()       


