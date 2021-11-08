import SQlite3

def insertFastRows(db):
    db.insert_row_EMPLOYEES("\"Henry\"", "\"Wilt\"", 19, 0)
    db.insert_row_EMPLOYEES("\"Dan\"", "\"Power\"", 41, 1)
    db.insert_row_EMPLOYEES("\"Ed\"", "\"Mansfield\"", 23, 0)
    db.insert_row_EMPLOYEES("\"Grace\"", "\"Wonne\"", 32, 0)
    db.insert_row_EMPLOYEES("\"Hef\"", "\"Moneuhue\"", 65, 1)
    db.insert_row_EMPLOYEES("\"Thomas\"", "\"Adams\"", 34, 0)
    
    
    employeeID = db.get_EmployeeID("\"Dan\"", "\"Power\"")
    db.insert_row_DEPENDENTS("\"Mark\"", "\"Power\"", employeeID, 13, 0)
    employeeID = db.get_EmployeeID("\"Dan\"", "\"Power\"")
    db.insert_row_DEPENDENTS("\"Tucker\"", "\"Power\"", employeeID, 16, 0)
    employeeID = db.get_EmployeeID("\"Grace\"", "\"Wonne\"")
    db.insert_row_DEPENDENTS("\"Parker\"", "\"Wonne\"", employeeID, 31, 1)
    employeeID = db.get_EmployeeID("\"Thomas\"", "\"Adams\"")
    db.insert_row_DEPENDENTS("\"Tom\"", "\"Adams\"", employeeID, 2, 0)
    
    
    employeeID = db.get_EmployeeID("\"Henry\"", "\"Wilt\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)
    employeeID = db.get_EmployeeID("\"Dan\"", "\"Power\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)
    employeeID = db.get_EmployeeID("\"Ed\"", "\"Mansfield\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)
    employeeID = db.get_EmployeeID("\"Grace\"", "\"Wonne\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)
    employeeID = db.get_EmployeeID("\"Hef\"", "\"Moneuhue\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)
    employeeID = db.get_EmployeeID("\"Thomas\"", "\"Adams\"")
    db.insert_row_INSURED("\"Medical\"", 20000, employeeID)


def print_tables(db):
    EMPLOYEES = db.get_table("EMPLOYEES")
    # PRINT OUT EMPLOYEE TABLE
    print("(EmpoyeeID, First Name, Last Name, Age, Smoker)")
    for employee in EMPLOYEES:
        print(employee)
    
    
    DEPENDENTS = db.get_table("DEPENDENTS")
    # PRINT OUT EMPLOYEE TABLE
    print("(DependentID, First Name, Last Name, EmployeeID, Age, Smoker)")
    for dependent in DEPENDENTS:
        print(dependent)
        
        
    INSURED = db.get_table("INSURED")    
    # PRINT OUT EMPLOYEE TABLE
    print("(InsuredID, Insurance Type, Coverage Amount, EmployeeID)")
    for insure in INSURED:
        print(insure)


def add_DEPENDENTS(db):
    DEPENDENTS = db.get_table("DEPENDENTS")
    for dependent in DEPENDENTS:
        InsuredID = db.get_InsuredID(None,None,dependent[3])
        db.insert_row_DEPENDENTCOVERAGE(InsuredID, dependent[0])
    
        
    
    get_dependentCoverage_table = '''SELECT DEPENDENTCOVERAGE.ID, InsuredID, EMPLOYEES.FirstName, EMPLOYEES.LastName, DependentID, DEPENDENTS.FirstName, DEPENDENTS.LastName
                                     FROM DEPENDENTCOVERAGE
                                     INNER JOIN INSURED
                                     ON DEPENDENTCOVERAGE.InsuredID = INSURED.ID
                                     INNER JOIN EMPLOYEES
                                     ON EMPLOYEES.ID = INSURED.EmployeeID
                                     INNER JOIN DEPENDENTS
                                     ON DEPENDENTS.ID = DEPENDENTCOVERAGE.DependentID;'''
    DEPENDENTCOVERAGE = db.query(get_dependentCoverage_table)
    print("(DependentCoverageId, InsuredID, FirstName, LastName, DependentID, FirstName, LastName)")
    for dependent in DEPENDENTCOVERAGE:
        print(dependent)
        


def main():
    EmployeeInsurance = SQlite3.Database("main.db")
    EmployeeInsurance.drop_tables("DEPENDENTCOVERAGE")
    EmployeeInsurance.drop_tables("EMPLOYEES")
    EmployeeInsurance.drop_tables("DEPENDENTS")
    EmployeeInsurance.drop_tables("INSURED")
    
    EmployeeInsurance.create_tables()
    
    insertFastRows(EmployeeInsurance)
    
    print_tables(EmployeeInsurance)
    
    add_DEPENDENTS(EmployeeInsurance)
    

if __name__ == "__main__":
    main()