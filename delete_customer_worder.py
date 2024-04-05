from connect_db import connect_db

def delete_customer_worder():
    conn = connect_db() #remove this colon in case youre doing what i do
    if conn:
        try:
            cursor = conn.cursor()

            # customer to be removed - needs to be an iterable
            customer_to_remove = (2, )

            # check if the customer has associated orders
            query = "SELECT * FROM Orders WHERE customer_id = %s"
            cursor.execute(query, customer_to_remove)
            orders = cursor.fetchall()
            # print(orders)
            if orders:
                # we dont want to delete customers with orders
                print("Cannot delete customer: Customer has associate orders")
            else:
                # if they dont have orders, we can kick em to the curb
                query = "DELETE FROM Customer WHERE customer_id = %s"

                # execute that query
                cursor.execute(query, customer_to_remove)
                conn.commit()
                print("Customer removed succesfully")        

        except Exception as e:
            print(f"error: {e}")

        finally:
            cursor.close()
            conn.close()

delete_customer_worder()


        