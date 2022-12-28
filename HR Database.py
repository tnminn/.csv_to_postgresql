'''
Script demonstrates how to:
 1) connect to PostgreSQL database
 2) create a new database
 3) create tables (in this instance 3)
 3) import .csv files into created tables

In a 'real world' project that would involve connecting/disconnecting to a
database multiple times, create or drop tables the author would wrap these
actions into functions for repeated use.

@author Tammy N. Minnebo
Created Tuesday, 12/27/2022

'''


import psycopg2

# connect to postgresql default database, create cursor, set auto commit
try:
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=postgres user=postgres password=password")
    print('Connection to the Postgres Database successful!')
except psycopg2.Error as e:
    print('Error: could not make connection to the Postgres database')
    print(e)

try:
    cur = conn.cursor()
    print('Cursor connection successful!')
except psycopg2.Error as e:
    print('Error: could not get cursor to the Database')
    print(e)

conn.set_session(autocommit=True)

# create the HR Database, close connection to default database and connect to
# new database, create cursor and set auto commit
try:
    cur.execute('create database HRData')
    print('Database creation successful!')
except psycopg2.Error as e:
    print('Error: could not create database')
    print(e)

try:
    conn.close()
    print('Connection to database is closed')
except psycopg2.Error as e:
    print('Error: could not close connection to database')
    print(e)

try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=hrdata user=postgres "
                            "password=password")
    print('Connection to database hrdata successful!')
except psycopg2.Error as e:
    print('Error: could not make connection to the database')
    print(e)

try:
    cur = conn.cursor()
    print('Cursor connection successful!')
except psycopg2.Error as e:
    print('Error: could not get cursor to the Database')
    print(e)

conn.set_session(autocommit=True)

# create the three tables (empdata, positions and departments) and import csv
# files in to populate tables
try:
    cur.execute('''CREATE TABLE IF NOT EXISTS EmpData (First varchar, 
    Last varchar, EmpID int, MarriedID int, MaritalStatusID int, EmpStatusID 
    int, DeptID int, PerfScoreID int, Salary int, Termd int, PositionID int, 
    State varchar, Zip int, DOB date, Sex varchar, MaritalDesc varchar, 
    DateofHire date, DateofTermination varchar, TermReason varchar, 
    EmploymentStatus varchar, ManagerName varchar, PerformanceScore varchar,
    EngagementSurvey float, EmpSatisfaction float, LastPerformanceReview_Date 
    date, DaysLateLast30 int, Absences int);''')

    print('Table created successfully!')
except psycopg2.Error as e:
    print('Error: Issue with creating table.')
    print(e)

try:
    with open(r'C:\Users\tammy\PycharmProjects\HR '
              r'Pipeline_PostgreSQL\employees.csv') as csvFile:
        next(csvFile)
        cur.copy_from(csvFile, 'empdata', sep=',')

    print('table copied from csv file successfully!')
except psycopg2.Error as e:
    print('Error: could not copy table from csv file')
    print(e)

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Positions (PositionID int, 
    Position varchar);''')

    print('Table created successfully!')
except psycopg2.Error as e:
    print('Error: Issue with creating table.')
    print(e)

try:
    with open(r'C:\Users\tammy\PycharmProjects\HR '
              r'Pipeline_PostgreSQL\positions.csv') as csvFile:
        next(csvFile)
        cur.copy_from(csvFile, 'positions', sep=',')

    print('table copied from csv file successfully!')
except psycopg2.Error as e:
    print('Error: could not copy table from csv file')
    print(e)

try:
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DepartmentID int, 
    Department varchar);''')

    print('Table created successfully!')
except psycopg2.Error as e:
    print('Error: Issue with creating table.')
    print(e)

try:
    with open(r'C:\Users\tammy\PycharmProjects\HR '
              r'Pipeline_PostgreSQL\departments.csv') as csvFile:
        next(csvFile)
        cur.copy_from(csvFile, 'departments', sep=',')

    print('table copied from csv file successfully!')
except psycopg2.Error as e:
    print('Error: could not copy table from csv file')
    print(e)
