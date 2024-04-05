from connect_db import connect_db

def fetch_orders_by_cutomer():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()
            # query to display all orders and the customers who made them
            query = """
            SELECT order_id, date, Customer.customer_id, name, email
            FROM Customer, Orders
            WHERE Customer.customer_id = Orders.customer_id;
                        
            """
            # specify orders by customer name
            # query = """
            # SELECT order_id, date, Customer.customer_id, name, email
            # FROM Customer, Orders
            # WHERE Customer.customer_id = Orders.customer_id AND name LIKE 'Obi%' ;
                        
            # """
            # execute query
            cursor.execute(query)

            # show all our orders with customer info
            for order in cursor.fetchall():
                print(order)
            
           
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
fetch_orders_by_cutomer()










