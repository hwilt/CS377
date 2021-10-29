import sqlite3

# stmt contains placeholder ?'s for params
# params is a tuple (val1, val2, ...)
def query(con, stmt, params=None):
    cur = con.cursor()
    if params is None:
        result = cur.execute(stmt)
    else:
        result = cur.execute(stmt, params)
    con.commit()
    return result


# Could not get working?
def userInput(con):
    select = input("Type 1 for Account, 2 for Product, 3 for Order: ")
    if select == 1:
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        query(con, "INSERT INTO ACCOUNTS (FirstName, LastName) VALUES (?, ?);", (fname, lname))
    elif select == 2:
        pname = input("Enter Product Name: ")
        price = input("Enter Price of Product: ")
        query(con, "INSERT INTO PRODUCTS (ProductName, Price) VALUES (?, ?);", (pname, price))
    elif select == 3:
        fname = input("Enter Customer's First Name: ")
        lname = input("Enter Customer's Last Name: ")
        product = input("Enter Product's Name: ")
        
        query(con, "SELECT * FROM ACCOUNTS WHERE FirstName = ? AND LastName = ?", (fname, lname))
        Account = res.fetchone()
        AccountID = Account[0]
        
        query(con, "SELECT * FROM PRODUCTS WHERE ?", (product))
        Product = res.fetchone()
        ProductID = Product[0]
        query(con, "INSERT INTO ORDERS (AccountID, ProductID) VALUES (?, ?);", (AccountID, ProductID))


con = sqlite3.connect('main.db')

res = query(con, "DROP TABLE IF EXISTS ORDERS;")
res = query(con, "DROP TABLE IF EXISTS ACCOUNTS;")
res = query(con, "DROP TABLE IF EXISTS PRODUCTS;")

#Making ORDERS table
res = query(con, "CREATE TABLE IF NOT EXISTS ORDERS (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, AccountID INTEGER NOT NULL, ProductID INTEGER NOT NULL, FOREIGN KEY(AccountID) REFERENCES ACCOUNTS(ID), FOREIGN KEY(ProductID) REFERENCES PRODUCT(ID));")
#Making ACCOUNTS table
res = query(con, "CREATE TABLE IF NOT EXISTS ACCOUNTS (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, FirstName TEXT NOT NULL, LastName TEXT NOT NULL);")
#Making PRODUCTS table
res = query(con, "CREATE TABLE IF NOT EXISTS PRODUCTS (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ProductName TEXT NOT NULL, Price REAL NOT NULL);")

# Putting data in the database so it populated more
res = query(con, "INSERT INTO ACCOUNTS (FirstName, LastName) VALUES (\"Henry\", \"Wilt\")")
res = query(con, "INSERT INTO ACCOUNTS (FirstName, LastName) VALUES (\"Ed\", \"Mansfield\")")
res = query(con, "INSERT INTO ACCOUNTS (FirstName, LastName) VALUES (\"Grace\", \"Wonne\")")

res = query(con, "INSERT INTO PRODUCTS (ProductName, Price) VALUES (\"Sprite\", 2.49)")
res = query(con, "INSERT INTO PRODUCTS (ProductName, Price) VALUES (\"Diet Coke\", 1.99)")
res = query(con, "INSERT INTO PRODUCTS (ProductName, Price) VALUES (\"Gum\", 0.99)")

res = query(con, "INSERT INTO ORDERS (AccountID, ProductID) VALUES (1, 2)")
res = query(con, "INSERT INTO ORDERS (AccountID, ProductID) VALUES (1, 1)")
res = query(con, "INSERT INTO ORDERS (AccountID, ProductID) VALUES (3, 1)")


# Asking user for input for DATABASE
pname = input("Enter Product Name: ")
price = input("Enter Price of Product: ")
res = query(con, "INSERT INTO PRODUCTS (ProductName, Price) VALUES (?, ?);", (pname, price))


res = query(con, "SELECT AVG(Price) AveragePrice FROM PRODUCTS;")
print("Avgerage Price of Products $" + str(res.fetchone()[0]))


con.close()