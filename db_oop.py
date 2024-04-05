from connect_db import connect_db
from fetch_customer import fetch_customers
class Customer():

    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_phone(self):
        return self.phone
    
    def get_address(self):
        return self.address

    
    


def add_customer(name, email, phone, address):    
    conn = connect_db()

    if conn:
        try:
            cursor = conn.cursor()

            insert_info = (name, email, phone, address)           

            # query to insert into Orders table
            query = "INSERT INTO Customer (name, email, phone, address) VALUES (%s, %s, %s, %s)"
            # execute query
            cursor.execute(query, insert_info)
            #              query, tuple with the above order information
            conn.commit()
            print(f"customer was succesfully added")
        except Exception as e:
            print(f"error: {e}")
        finally:
            cursor.close()
            conn.close()
def run():
    while True:
        action = input("Enter 'add' to add a customer or quit to quit").lower()
        if action == "add":
            name = input("What is the name of your customer? ")
            email = input("What is the customer's email? ")
            phone = input("What is the customer's phone? ")
            address = input("What is the customer's address? ")
            customer = Customer(name, email, phone, address)
            # we could use the variables we set above and pass those into add_customer
            # accessing class attributes and sending them to a database
            add_customer(customer.get_name(), customer.get_email(), customer.get_phone(), customer.get_address())
        elif action == "quit":
            print("Have a nice day, here are your customers:")
            fetch_customers()
            break
        else:
            print("Please enter a valid input!")

run()



