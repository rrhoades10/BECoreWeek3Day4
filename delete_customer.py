from connect_db import connect_db

def delete_customer():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            # customer to be deleted
            # this needs to be a tuple
            del_customer = (2,) #reflect the customer_id
            query = "DELETE FROM Customer WHERE customer_id = %s"
            cursor.execute(query, del_customer)
            conn.commit()
            print("Customer succesfully removed")

        except Exception as e:
            print(f"error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_customer()




