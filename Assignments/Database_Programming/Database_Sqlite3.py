###########################################
# Created by; Henry Wilt                  #
# October 28th. 2021                      #
###########################################

import sqlite3

class SqliteDatabase():
    
    ###########################################
    #              Helper Methods             #
    ###########################################
    
    ###########################################
    # constructor method                      #
    #                                         # 
    # params;                                 #
    # db_path - Where the database is located #
    ###########################################
    def __init__(self, db_path=None):
        
        self.conn = None
        self.cursor = None
        
        if db_path:
            self.open(db_path)
    
    ###########################################
    # open method                             #
    # Connects to the database file and       #
    # creates a cursor                        #
    #                                         # 
    # params;                                 #
    # db_path - Where the database is located #
    ###########################################
    def open(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    
    ###########################################
    # close method                            #
    # Commits any excuted queries then closes #
    # the connection to the database file     #
    #                                         # 
    # params;                                 #
    # None                                    #
    ###########################################    
    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            

    ###########################################
    # drop_tables method                      #
    # Will drop the table you put as a param  #
    #                                         # 
    # params;                                 #
    # table_name - name of table you want     #
    #              droped                     #
    ###########################################
    def drop_tables(self, table_name):
        sql_drop = "DROP TABLE IF EXISTS " + table_name + ";"
        self.query(sql_drop)
    
        
    ###########################################
    # query method                            #
    # Excute a sql statement                  #
    #                                         # 
    # params;                                 #
    # stmt - sql statement in string form     #
    # params                                  #
    ###########################################
    def query(self, stmt, params=None):
        if params:
             res = self.cursor.execute(stmt, params)
        else:
            res = self.cursor.execute(stmt)
        self.conn.commit()
        return res
    
    ###########################################
    # get_table method                        #  
    # Will get the data from the table        #
    #                                         # 
    # params;                                 #
    # table_name - name of table you want     #
    #              to get                     #
    ###########################################
    def get_table(self, table_name):
        res = self.query("SELECT * FROM " + str(table_name) + ";")
        result = res.fetchall()
        return result
        
    
    ###########################################
    #       Database Speicfic Methods         #
    ###########################################


    ###########################################
    # create_tables method                    #
    # Will create a sqlite table              #
    # TODO: USE PARAMS TO CREATE THE TABLE    #
    #       INSTEAD OF WRITING THE SQL IN     #
    #       METHOD                            #
    #                                         # 
    # params;                                 #
    # stmt - sql statement in string form     #
    #                                         #
    ###########################################
    def create_tables(self):
        #Making ORDERS table
        self.query('''CREATE TABLE IF NOT EXISTS ORDERS (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                AccountID INTEGER NOT NULL, 
                                ProductID INTEGER NOT NULL, 
                                FOREIGN KEY(AccountID) REFERENCES ACCOUNTS(ID), 
                                FOREIGN KEY(ProductID) REFERENCES PRODUCT(ID)
                            );''')
        
        #Making ACCOUNTS table
        self.query('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                FirstName TEXT NOT NULL, 
                                LastName TEXT NOT NULL
                            );''')
        
        #Making PRODUCTS table
        self.query('''CREATE TABLE IF NOT EXISTS PRODUCTS (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                ProductName TEXT NOT NULL, 
                                Price REAL NOT NULL
                            );''')
        
    ###########################################
    # insert_row_ORDERS method                #
    # Inserts a new row into the ORDER table  #
    #                                         # 
    # params;                                 #
    # AccountID - the id of the Customer Acc. #
    # ProductID - the id of the Product       #
    ###########################################
    def insert_row_ORDERS(self, AccountID, ProductID):
        self.query("INSERT INTO ORDERS (AccountID, ProductID) VALUES (" + str(AccountID) + ", " + str(ProductID) + ");")
    
    ###########################################
    # insert_row_ACCOUNTS method              #
    # Inserts a new row into the Acc. table   #
    #                                         # 
    # params;                                 #
    # fname - first name of the Customer      #
    # lname - last name of the Customer       #
    ###########################################
    def insert_row_ACCOUNTS(self, fname, lname):
        self.query("INSERT INTO ACCOUNTS (FirstName, LastName) VALUES (" + str(fname) + ", " + str(lname) + ");")
    
    ###########################################
    # insert_row_PRODUCTS method              #
    # Inserts a new row into the PRODUCT table#
    #                                         # 
    # params;                                 #
    # ProductName - name of product           #
    # Price - the price of the product        #
    ###########################################
    def insert_row_PRODUCTS(self, ProductName, Price):
        self.query("INSERT INTO PRODUCTS (ProductName, Price) VALUES (" + str(ProductName) + ", " + str(Price) + ");")

    
    ###########################################
    # get_row_ORDERS method                   #
    # gets an existing row from the ORDER     #
    #                                         # 
    # params;                                 #
    # AccountID - the id of the Customer Acc. #
    # ProductID - the id of the Product       #
    ###########################################
    def get_row_ORDERS(self, AccountID, ProductID):
        stmt = "SELECT * FROM ORDERS WHERE AccountID = " + str(AccountID) + " AND ProductID = " + str(ProductID) + ";"
        return self.query(stmt)
        
    ###########################################
    # get_row_ACCOUNTS method                 #
    # gets an existing row from the Acc. table#
    #                                         # 
    # params;                                 #
    # fname - first name of the Customer      #
    # lname - last name of the Customer       #
    ###########################################
    def get_row_ACCOUNTS(self, fname, lname):
        stmt = "SELECT * FROM ACCOUNTS WHERE FirstName = " + str(fname) + " AND LastName = " + str(lname) + ";"
        return self.query(stmt)
    
    ###########################################
    # get_row_PRODUCTS method                 #
    # gets an existing row from the PRODUCT   #
    #                                         # 
    # params;                                 #
    # ProductName - name of product           #
    # Price - the price of the product        #
    ###########################################
    def get_row_PRODUCTS(self, ProductName, Price):
        stmt = "SELECT * FROM PRODUCTS WHERE ProductName = " + str(ProductName) + " AND Price = " + str(Price) + ";"
        return self.query(stmt)    

