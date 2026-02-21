CREATE TABLE Store (
  store_id INT NOT NULL,
  store_name VARCHAR(40) NOT NULL,
  PRIMARY KEY (store_id)
);

INSERT INTO Store 
    (store_id, store_name)
	
VALUES
	(1111,'Red Store'),
	(1112,'Blue Store'),
	(1113,'Green Store'),
	(1114,'Orange Store'),
	(1115,'Pink Store'),
	(1116,'Brown Store'),
	(1117,'Purple Store');

CREATE TABLE Sales (
  sales_id INT NOT NULL,
  year INT NOT NULL,
  month INT NOT NULL,
  country VARCHAR(40) NOT NULL,
  store_id INT NOT NULL,
  sales_amount INT NOT NULL,
  PRIMARY KEY (sales_id),
  CONSTRAINT fk_store_id
      FOREIGN KEY(store_id) 
	  REFERENCES Store(store_id)
);

INSERT INTO Sales 
    (sales_id, year,month, country, store_id, sales_amount) 
VALUES 
    (1,2019,1,'Canada',1111,1000),
	(2,2020,3,'Canada',1112,5000),
	(3,2019,4,'Canada',1113,700),
	(4,2019,2,'Mexico',1114,8000),
	(5,2020,5,'Mexico',1115,100),
	(6,2019,1,'United States',1116,2000),
	(7,2020,5,'United States',1117,150),
	(8,2019,6,'Canada',1111,1000),
	(9,2020,6,'United States',1116,500),
	(10,2020,1,'Mexico',1114,8000),
	(11,2019,2,'Mexico',1115,500),
    (12,2020,4,'Mexico',1115,500);

-- 1. Retrieve the Sales table data with only the sales_id, store_id and sales_amount columns.


-- 2. Retrieve all of the sales for the 'Pink' store for 2019 in Mexico (all columns from the Sales and Store tables).


-- 3. Retrieve the total number of sales per store for the year 2019 (store_id, total_sales).


-- 4. Retrieve the store_names which had more than 1 sales for the year 2019 (store_name, count_of_sales).


-- 5. Create an index on Sales that would make your query from Question 2 more efficient. 