from connect_db import connect_db

def fetch_customers():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # query variable
            query = "SELECT * FROM Customer"

            # execute query
            cursor.execute(query)
            # looping through data
            for row in cursor.fetchall():
                print(row)

        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    do_this = fetch_customers
    do_this()