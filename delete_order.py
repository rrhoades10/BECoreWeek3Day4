from connect_db import connect_db

def delete_order():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # set order information to be deleted
            customer_id = 2
            # order_id to be deleted
            order_id = 4

            # sql query to delete
            query = "DELETE FROM Orders WHERE order_id = %s AND customer_id = %s"

            cursor.execute(query, (order_id, customer_id))
            conn.commit()
            print("Order was succesfully deleted")           
           
                      

        except Exception as e:
            print(f"and error occurred: {e}") 
        
        finally:
            cursor.close()
            conn.close()
delete_order()       
