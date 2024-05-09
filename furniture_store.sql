CREATE DATABASE  `furniturestore`;
USE `furniturestore`;

CREATE TABLE `customer` (
  `Customer_ID` int NOT NULL,
  `Customer_Name` varchar(30) DEFAULT NULL,
  `Customer_Email` varchar(30) DEFAULT NULL,
  `Customer_PhNo` char(10) DEFAULT NULL,
  `Customer_Address` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`Customer_ID`)
);

CREATE TABLE `employee` (
  `Emp_ID` int NOT NULL,
  `Emp_Name` varchar(30) DEFAULT NULL,
  `Emp_PhNo` char(10) DEFAULT NULL,
  `Emp_Position` varchar(20) DEFAULT NULL,
  `Emp_Email` varchar(30) DEFAULT NULL,
  `Emp_Sal` int DEFAULT NULL,
  PRIMARY KEY (`Emp_ID`)
);

CREATE TABLE `feedback` (
  `Feedback_ID` int NOT NULL AUTO_INCREMENT,
  `Order_ID` int DEFAULT NULL,
  `Rating` int DEFAULT NULL,
  `Text_Feedback` text,
  `Date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Feedback_ID`)
);

CREATE TABLE `offer` (
  `offer_id` int NOT NULL AUTO_INCREMENT,
  `offer_type` varchar(100) NOT NULL,
  `discount_percentage` decimal(5,2) NOT NULL,
  `product_included` varchar(100) NOT NULL,
  `conditions` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`offer_id`)
);

CREATE TABLE `product` (
  `Prod_ID` int NOT NULL,
  `Prod_Name` varchar(20) NOT NULL,
  `Prod_Descp` varchar(30) DEFAULT NULL,
  `Prod_Price` int DEFAULT NULL,
  `StockID` int DEFAULT NULL,
  PRIMARY KEY (`Prod_ID`),
  KEY `StockID` (`StockID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`StockID`) REFERENCES `stock` (`Stock_ID`)
);

CREATE TABLE `purchase` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) DEFAULT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `order_id` (`order_id`)
);

CREATE TABLE `stock` (
  `Stock_ID` int NOT NULL,
  `Stock_Capacity` int NOT NULL,
  `Stock_Avail` int DEFAULT NULL,
  PRIMARY KEY (`Stock_ID`)
);

CREATE TABLE `storedetails` (
  `Branch_ID` int NOT NULL,
  `Store_Branch` varchar(30) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Contact` char(10) DEFAULT NULL,
  `Manager_ID` int DEFAULT NULL,
  PRIMARY KEY (`Branch_ID`)
);

CREATE TABLE `supplier` (
  `Supplier_ID` int NOT NULL,
  `Supplier_Name` varchar(30) DEFAULT NULL,
  `Supplier_PhNo` char(10) DEFAULT NULL,
  `Supplier_Address` varchar(60) DEFAULT NULL,
  `Emp_incharge` int DEFAULT NULL,
  PRIMARY KEY (`Supplier_ID`)
);
