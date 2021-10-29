.header on
.mode column

-- Product Table
CREATE TABLE PRODUCT (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Product_Name TEXT NOT NULL, "Weight(g)" INTEGER NOT NULL, Price INTEGER);

INSERT INTO PRODUCT (Product_Name, "Weight(g)", Price) VALUES ("Phone", 170, 899);
INSERT INTO PRODUCT (Product_Name, "Weight(g)", Price) VALUES ("Phone Case", 100, 50);
INSERT INTO PRODUCT (Product_Name, "Weight(g)", Price) VALUES ("Headphones", 38, 25);
INSERT INTO PRODUCT (Product_Name, "Weight(g)", Price) VALUES ("Charger", 23, 10);

-- Customer Table
CREATE TABLE CUSTOMER (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, First_Name TEXT NOT NULL, Last_Name TEXT NOT NULL);

INSERT INTO CUSTOMER (First_Name, Last_Name) VALUES ("John", "Smith");
INSERT INTO CUSTOMER (First_Name, Last_Name) VALUES ("Bob", "Saget");
INSERT INTO CUSTOMER (First_Name, Last_Name) VALUES ("John", "Delia");


-- Print out Product and Customer Tables
SELECT * FROM PRODUCT;
SELECT * FROM CUSTOMER;

-- Link the Tables Together with Primary and Foreign Keys
CREATE TABLE "ORDER" (
  ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
  CustomerID INTEGER NOT NULL, 
  ProductID INTEGER NOT NULL,
	"Date" TEXT NOT NULL, 
  FOREIGN KEY(CustomerID) REFERENCES CUSTOMER(ID), 
  FOREIGN KEY(ProductID) REFERENCES PRODUCT(ID)
);

INSERT INTO "ORDER"(CustomerID, ProductID, "Date") VALUES (1, 1, "2021-07-10");
INSERT INTO "ORDER"(CustomerID, ProductID, "Date") VALUES (2, 1, "2001-01-01");
INSERT INTO "ORDER"(CustomerID, ProductID, "Date") VALUES (1, 2, "2021-07-10");
INSERT INTO "ORDER"(CustomerID, ProductID, "Date") VALUES (1, 4, "2021-07-10");
INSERT INTO "ORDER"(CustomerID, ProductID, "Date") VALUES (3, 1, "2021-04-20");

SELECT * FROM "ORDER";


-- Join
SELECT * FROM "ORDER" 
  INNER JOIN CUSTOMER
    ON CUSTOMER.ID = "ORDER".CustomerID
  INNER JOIN PRODUCT
    ON PRODUCT.ID = "ORDER".ProductID;


-- AVG Cost of an Order for the first customer
SELECT 
  COUNT("ORDER".ID) AS NumOrders, 
  AVG(PRODUCT.Price) AS AvgCost 
FROM "ORDER"
  INNER JOIN PRODUCT
    ON PRODUCT.ID = "ORDER".ProductID
WHERE CustomerID = 1


