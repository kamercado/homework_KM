-- Use the information you have to create a table schema for each of the six CSV files.
-- Remember to specify data types, primary keys, foreign keys, and other constraints.

-- Import each CSV file into the corresponding SQL table.

CREATE TABLE departments(
dept_no VARCHAR(4) PRIMARY KEY,
dept_name VARCHAR NOT NULL);

CREATE TABLE dept_emp(
emp_no INTEGER NOT NULL,
dept_no VARCHAR(4) NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL);

CREATE TABLE dept_manager(
dept_no VARCHAR(4) NOT NULL,
emp_no INTEGER PRIMARY KEY,
from_date DATE NOT NULL,
to_date DATE NOT NULL);

CREATE TABLE employees(
emp_no INTEGER PRIMARY KEY,
birth_date DATE NOT NULL,
first_name VARCHAR NOT NULL,
last_name VARCHAR NOT NULL,
gender VARCHAR(1) NOT NULL,
hire_date VARCHAR NOT NULL);

CREATE TABLE titles(
emp_no INTEGER NOT NULL,
title VARCHAR NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL);

CREATE TABLE salaries(
emp_no INTEGER PRIMARY KEY,
salary INTEGER NOT NULL,
from_date DATE NOT NULL,
to_date DATE NOT NULL);