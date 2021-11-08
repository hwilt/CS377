###########################################
# Created by; Henry Wilt                  #
# November 7th. 2021                      #
###########################################

import sqlite3

class Database():
    
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
        # Making the Employees table
        self.query('''CREATE TABLE IF NOT EXISTS EMPLOYEES (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                FirstName TEXT NOT NULL, 
                                LastName TEXT NOT NULL, 
                                Age INTEGER NOT NULL, 
                                Smoker Integer DEFAULT 0 NOT NULL
                            );''')
        
        # Making the Dependents table
        self.query('''CREATE TABLE IF NOT EXISTS DEPENDENTS (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                FirstName TEXT NOT NULL, 
                                LastName TEXT NOT NULL,
                                EmployeeID INTEGER NOT NULL,
                                Age INTEGER NOT NULL, 
                                Smoker Integer DEFAULT 0 NOT NULL,
                                FOREIGN KEY(EmployeeID) REFERENCES EMPLOYEES(ID)
                            );''')
        
        # Making the Insured table
        self.query('''CREATE TABLE IF NOT EXISTS INSURED (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                InsuranceType TEXT NOT NULL, 
                                CoverageAmount REAL, 
                                EmployeeID INTEGER NOT NULL, 
                                FOREIGN KEY(EmployeeID) REFERENCES EMPLOYEES(ID)
                            );''')
        
        # Making the Dependtcoverage table
        self.query('''CREATE TABLE IF NOT EXISTS DEPENDENTCOVERAGE (
                                ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                InsuredID INTEGER NOT NULL, 
                                DependentID INTEGER NOT NULL, 
                                FOREIGN KEY(InsuredID) REFERENCES INSURED(ID), 
                                FOREIGN KEY(DependentID) REFERENCES DEPENDENTS(ID)
                            );''')
        
        
    def insert_row_EMPLOYEES(self, fname, lname, age, smoker):
        self.query("INSERT INTO EMPLOYEES (FirstName, LastName, Age, Smoker) VALUES (" + str(fname) + "," + str(lname) + "," + str(age) + "," + str(smoker) + ");")
        
    def insert_row_DEPENDENTS(self, fname, lname, employeeID, age, smoker):
        self.query("INSERT INTO DEPENDENTS (FirstName, LastName, EmployeeID, Age, Smoker) VALUES (" + str(fname) + "," + str(lname) + "," + str(employeeID) + "," + str(age) + "," + str(smoker) + ");")
        
    def insert_row_INSURED(self, InsuranceType, CoverageAmount, EmployeeID):
        self.query("INSERT INTO INSURED(InsuranceType, CoverageAmount, EmployeeID) VALUES (" + str(InsuranceType) + "," + str(CoverageAmount) + "," + str(EmployeeID) + ");")
        
    def insert_row_DEPENDENTCOVERAGE(self, InsuredID, DependentID):
        self.query("INSERT INTO DEPENDENTCOVERAGE(InsuredID, DependentID) VALUES (" + str(InsuredID) + "," + str(DependentID) + ");")

    def get_row_EMPLOYEES(self, fname, lname):
        stmt = "SELECT * FROM EMPLOYEES WHERE FirstName = " + str(fname) + " AND LastName = " + str(lname) + ";"
        return self.query(stmt)
    
    def get_EmployeeID(self, fname, lname):
        stmt = "SELECT * FROM EMPLOYEES WHERE FirstName = " + str(fname) + " AND LastName = " + str(lname) + ";"
        results = self.query(stmt)
        return results.fetchone()[0]
    
    def get_row_DEPENDENTS(self, fname = None, lname = None, EmployeeID = None):
        if EmployeeID:
            stmt = "SELECT * FROM DEPENDENTS WHERE EmployeeID = " + str(EmployeeID) + ";"
            ret = self.query(stmt)
        else:
            stmt = "SELECT * FROM DEPENDENTS WHERE FirstName = " + str(fname) + " AND LastName = " + str(lname) + ";"
            ret = self.query(stmt)
        return ret
        
    def get_DependentID(self, fname, lname):
        stmt = "SELECT * FROM DEPENDENTS WHERE FirstName = " + str(fname) + " AND LastName = " + str(lname) + ";"
        results = self.query(stmt)
        return results.fetchone()[0]
    
    def get_row_INSURED(self, fname = None, lname = None, EmployeeID = None):
        if EmployeeID is None:
            EmployeeID = self.get_EmployeeID(fname, lname)
        
        stmt = "SELECT * FROM INSURED WHERE EmployeeID = " + str(EmployeeID) + ";"
        return self.query(stmt) 
    
    def get_InsuredID(self, fname = None, lname = None, EmployeeID = None):
        if EmployeeID is None:
            EmployeeID = self.get_EmployeeID(fname, lname)
        
        stmt = "SELECT * FROM INSURED WHERE EmployeeID = " + str(EmployeeID) + ";"
        results = self.query(stmt)
        return results.fetchone()[0]
    
    def get_row_DEPENDENTCOVERAGE(self, InsuredID = None, DependentID = None):
        if InsuredID:
            stmt = "SELECT * FROM DEPENDENTCOVERAGE WHERE InsuredID = " + str(InsuredID) + ";"
        else:
            stmt = "SELECT * FROM DEPENDENTCOVERAGE WHERE DependentID = " + str(DependentID) + ";"
        return self.query(stmt)
    
    
    
    
    
    
    
    