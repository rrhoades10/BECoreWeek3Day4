from connect_db import connect_db

def fetch_orders():
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM Orders"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)
           
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
fetch_orders()










