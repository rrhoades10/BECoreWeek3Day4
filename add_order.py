from connect_db import connect_db

def add_order():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            # set order information into variables
            omen_id = 8
            order_date = "2024-04-05"

            # query to insert into Orders table
            query = "INSERT INTO Orders (date, customer_id) VALUES (%s, %s)"
            # execute query
            cursor.execute(query, (order_date, omen_id))
            #              query, tuple with the above order information
            conn.commit()
            print(f"order was succesfully added for Omen")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
add_order()










