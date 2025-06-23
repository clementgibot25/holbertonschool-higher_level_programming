# SQL Introduction: Key Concepts and MySQL Usage

## 1. What’s a Database?
A **database** is an organized collection of data, generally stored and accessed electronically from a computer system. Databases allow you to efficiently store, retrieve, and manage data.

## 2. What’s a Relational Database?
A **relational database** is a type of database that stores data in tables (relations) with rows and columns. Each table represents an entity, and relationships between tables are established using keys. Relational databases use Structured Query Language (SQL) to manage and manipulate data.

## 3. What Does SQL Stand For?
**SQL** stands for **Structured Query Language**. It is the standard language used to interact with relational databases for tasks such as querying, updating, and managing data.

## 4. What’s MySQL?
**MySQL** is an open-source relational database management system (RDBMS) that uses SQL as its query language. It is widely used for web applications and supports large-scale database operations.

## 5. How to Create a Database in MySQL
To create a database in MySQL, use the following command:
```sql
CREATE DATABASE database_name;
```
Example:
```sql
CREATE DATABASE hbnb_dev_db;
```

## 6. What Does DDL and DML Stand For?
- **DDL**: Data Definition Language (e.g., CREATE, ALTER, DROP) — commands that define or modify database structures.
- **DML**: Data Manipulation Language (e.g., SELECT, INSERT, UPDATE, DELETE) — commands that manage data within tables.

## 7. How to CREATE or ALTER a Table
- **CREATE TABLE**: Defines a new table and its columns.
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
```
- **ALTER TABLE**: Modifies an existing table (add, modify, or drop columns).
```sql
ALTER TABLE users ADD COLUMN age INT;
```

## 8. How to SELECT Data from a Table
To retrieve data:
```sql
SELECT * FROM users;
SELECT name, email FROM users WHERE age > 18;
```

## 9. How to INSERT, UPDATE, or DELETE Data
- **INSERT**:
```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
```
- **UPDATE**:
```sql
UPDATE users SET email = 'newemail@example.com' WHERE name = 'Alice';
```
- **DELETE**:
```sql
DELETE FROM users WHERE name = 'Alice';
```

## 10. What Are Subqueries?
A **subquery** is a query nested inside another SQL query. Subqueries can be used in SELECT, INSERT, UPDATE, or DELETE statements.
Example:
```sql
SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE amount > 100);
```

## 11. How to Use MySQL Functions
MySQL provides built-in functions for calculations, string manipulation, date/time operations, etc.
Examples:
```sql
SELECT COUNT(*) FROM users;
SELECT UPPER(name) FROM users;
SELECT NOW();
SELECT AVG(price) FROM products;
```

---

This README gives an overview of fundamental database concepts and practical MySQL usage. For more details, refer to the [MySQL documentation](https://dev.mysql.com/doc/).
