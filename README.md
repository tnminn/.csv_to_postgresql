# .csv_to_postgresql
This is a quick demonstration of how to load a .csv file into tables of a postgresql database and tables.

To install and run, you will need:

Postgresql
Python (with psycopg2 library installed)
3 data files (employees, positions and departments), located in the project repository

Tests:
In postgresql shell you can input the sql queries listed below to check:
1) if you have created a database
2) if you have created 3 tables in your database
3) if you have inserted data in your tables

sql queries:

1) to view all databases >> postgres =# \dt

2) to view all tables within the database, first switch to that database, then display the tables list

>> postgres=# \c [name of database] 
>> [name of database]=# \dt

3) to verify information was inserted >> [name of database]-# select * from [table name] limit 10;

