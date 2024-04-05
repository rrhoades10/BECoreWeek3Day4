from connect_db import connect_db

def update_order():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            
            # setting order details
            customer_id = 3
            order_id = 5 #order_id we are updating
            new_order_date = "2024-04-05"
            update_info = (new_order_date, order_id, customer_id)

            # Query to update
            query = "UPDATE Orders SET DATE = %s WHERE order_id = %s AND customer_id = %s "
            cursor.execute(query, (new_order_date, order_id, customer_id) )
            #                         same thing as including update_info from line 13
            conn.commit()
            print("Your order was succesfully updated!")           

        except Exception as e:
            print(f"and error occurred: {e}") 
        
        finally:
            cursor.close()
            conn.close()
update_order()       


