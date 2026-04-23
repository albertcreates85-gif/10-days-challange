-- check if table is already present 
drop table if exists retail_sales;

-- creating table
create table retail_sales(
  transactions_id int primary key,
  sale_date date,
  sale_time time,
  customer_id int,
  gender varchar(15),
  age int,
  category varchar(15),
  quantiy int,
  price_per_unit float,
  cog float,
  total_sale float
  
);

-- looking for head 
select * from retail_sales
limit 5;

-- countinge the total rows
select count(*)

-- data cleaning 

select * 
from retail_sales 
where transactions_id is null
    or
    sale_date is null
    or
    sale_time is null
    or
    gender is null
    or
    category is null
    or
    quantiy is null
    or
    cog is null
    or
    total_sale is null;

-- deleting the null rows
delete from retail_sales 
where  transactions_id is null
    or
    sale_date is null
    or
    sale_time is null
    or
    gender is null
    or
    category is null
    or
    quantiy is null
    or
    cog is null
    or
    total_sale is null;

-- how many sales we have 
select count(*) as total_sales from retail_sales;


-- how many distinct category we have 
select distinct category from retail_sales;

-- now how they are distributed or whats their counts 
select distinct category ,count(category) as categroy_count
from retail_sales
group by category;

-- what is the frequency distribution by gender 
select gender ,count(gender) 
from retail_sales
group by gender ;

-- Write a SQL query to calculate the total sales (total_sale) for each category.
select category,
       sum(total_sale) as net_sale,
	   count(*) as total_orders
from retail_sales
group by category;

-- what is the mean age group by each category
select category,
floor(avg(age)) as mean_age
from retail_sales
group by category;

-- in 2022/2023 which category dominated on their revenue 
SELECT 
category ,
net_sale
FROM (
    SELECT 
        category ,
		sum(total_sale) as net_sale,
        EXTRACT(YEAR FROM sale_date) AS year_of_sale
    FROM retail_sales
	group by category , extract(year from sale_date)
) t
WHERE year_of_sale = 2023
order by net_sale desc;

-- SQL query to find all transactions where the total_sale is greater than 1000.

SELECT * FROM retail_sales
WHERE total_sale > 1000

 -- what are the  total number of transactions (transaction_id) made by each gender in each category.
select category ,
 gender ,
 count(*) as total_trans
 from retail_sales
 group by category , gender 
 order by 1;

-- what are the outliers in total sales show their customer id 
select customer_id , category
from retail_sales
where total_sale >= 1500 or total_sale <= 50
order by category;

-- query to find the top 5 customers based on the highest total sales 

SELECT 
    customer_id,
    SUM(total_sale) as total_sales
FROM retail_sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

 -- query to find the number of unique customers who purchased items from each category.
SELECT 
    category,    
    COUNT(DISTINCT customer_id) as cnt_unique_cs
FROM retail_sales
GROUP BY category;

-- query to calculate the average sale for each month. Find out best selling month in each year
select 
yearOfSale,
monthOfSale,
net_sale
from (
select 
extract(year from sale_date) as yearOfSale,
extract(month from sale_date) as monthOfSale,
avg(total_sale) as net_sale,
rank() over(partition by extract(year from sale_date) order by avg(total_sale) desc) as rnk
from retail_sales
group by 1 , 2) as t
where rnk = 1;

