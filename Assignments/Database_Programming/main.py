import Database_Sqlite3


def insertFastRows(database):
    database.insert_row_ACCOUNTS("\"Henry\"", "\"Wilt\"")
    database.insert_row_ACCOUNTS("\"Ed\"", "\"Mansfield\"")
    database.insert_row_ACCOUNTS("\"Grace\"", "\"Wonne\"")
    
    database.insert_row_PRODUCTS("\"Sprite\"", 2.49)
    database.insert_row_PRODUCTS("\"Diet Coke\"", 1.99)
    database.insert_row_PRODUCTS("\"Gum\"", 0.99)
    
    database.insert_row_ORDERS(1, 2)
    database.insert_row_ORDERS(1, 1)
    database.insert_row_ORDERS(3, 1)


def print_tables(database):
    ACCOUNTS = database.get_table("ACCOUNTS")
    PRODUCTS = database.get_table("PRODUCTS")
    get_order_table = '''SELECT ORDERS.ID, FirstName, LastName, ProductName, Price
                             FROM ORDERS
                             INNER JOIN ACCOUNTS
                             ON ACCOUNTS.ID = ORDERS.AccountID
                             INNER JOIN PRODUCTS
                             ON PRODUCTS.ID = ORDERS.ProductID;'''
    ORDERS = database.query(get_order_table)
    
    #Print out the ACCOUNT TABLE
    print("(AccountID, First Name, Last Name)")
    for account in ACCOUNTS:
        print(account)
    
    #Print out the PRODUCT TABLE
    print("\n(ProductID, Product Name, Price)")
    for product in PRODUCTS:
        print(product)
    
    #Print out the ORDER TABLE
    print("\n(OrderID, AccountID, ProductID)")
    for order in ORDERS:
        print(order)


def aggregated_Queries(database):
    
    # First Aggregated Query: Average price of products in store
    results = database.query("SELECT AVG(Price) AveragePrice FROM PRODUCTS;")
    print("\nAvgerage Price of Products $" + str(round(results.fetchone()[0],2)))
    
    # Second Aggregated Query: Average price of Order
    stmt = '''SELECT AVG(PRICE) AverageOrder FROM ORDERS
                    INNER JOIN PRODUCTS ON PRODUCTS.ID = ORDERS.ProductID;
            '''
    results = database.query(stmt)
    print("\nAvgerage Price of Orders $" + str(round(results.fetchone()[0],2)))
    
    #Third Aggregated Query: Sum Price of Orders
    stmt = '''SELECT SUM(PRICE) AverageOrder FROM ORDERS
                    INNER JOIN PRODUCTS ON PRODUCTS.ID = ORDERS.ProductID;
            '''
    results = database.query(stmt)
    print("\nTotal Cost of Orders $" + str(round(results.fetchone()[0],2)))
    

def main():
    Orders_Database = Database_Sqlite3.SqliteDatabase("main.db")
    Orders_Database.drop_tables("ORDERS")
    Orders_Database.drop_tables("ACCOUNTS")
    Orders_Database.drop_tables("PRODUCTS")
    
    Orders_Database.create_tables()
    
    insertFastRows(Orders_Database)
    
    print_tables(Orders_Database)
    
    aggregated_Queries(Orders_Database)
    
    Orders_Database.close()
    
    
if __name__ == "__main__":
    main()