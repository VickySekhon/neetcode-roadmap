CREATE TABLE Store (
     store_id INT NOT NULL,
     store_name VARCHAR(40) NOT NULL,
     client_id INT NOT NULL,
     PRIMARY KEY (store_id),
     CONSTRAINT fk_client_id
          FOREIGN KEY(client_id)
          REFERENCES Clients(client_id)
);

INSERT INTO Store (store_id, store_name, client_id)
VALUES
     (10, "something", 2839044);


-- 1. Retrieve the Sales table data with only the sales_id, store_id and sales_amount columns.
SELECT sales_id, store_id, sales_amount FROM Sales;

-- 2. Retrieve all of the sales for the 'Pink' store for 2019 in Mexico (all columns from the Sales and Store tables).
SELECT sls.*
FROM Sales sls INNER JOIN Store stor ON sls.store_id = stor.id
WHERE stor.Store_name = "Pink Store"
AND sls.year = 2019
AND sls.country = "Mexico";


-- 3. Retrieve the total number of sales per store for the year 2019 (store_id, total_sales).
SELECT Count(*) as "total sales", str.store_name 
FROM Sales s join Store str ON s.store_id = str.store_id
WHERE s.year = 2019
GROUP BY store_id;


-- 4. Retrieve the store_names which had more than 1 sales for the year 2019 (store_name, count_of_sales).
select s.store_name
FROM Store s join Sales sl on s.store_id = sl.store_id
WHERE sl.year = 2019
GROUP BY s.store_name
HAVING count(*) > 1;

-- 5. Create an index on Sales that would make your query from Question 2 more efficient.
create index db_indx_store_name_sales_year_sales_country
ON (sls.Store_name, sls.year, sls.country)
FROM Sales sls JOIN Store stor sls.store_id = stor.id
