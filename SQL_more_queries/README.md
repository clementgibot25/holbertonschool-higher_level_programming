# SQL & MySQL Concepts: Quick Reference

## 1. How to Create a New MySQL User

To create a new user in MySQL, use the following SQL command:

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

- `username`: the name of the new user.
- `host`: where the user can connect from (use `'localhost'` for local, `'%'` for any host).
- `password`: the user's password.

**Example:**
```sql
CREATE USER 'alice'@'localhost' IDENTIFIED BY 'mySecret123';
```

## 2. How to Manage Privileges for a User to a Database or Table

Grant privileges with the `GRANT` statement:

```sql
GRANT privilege_type ON database.table TO 'username'@'host';
```

- `privilege_type`: e.g., `ALL`, `SELECT`, `INSERT`, `UPDATE`, etc.
- `database.table`: specify database and table, or use `*.*` for all.

**Example:**
```sql
GRANT ALL PRIVILEGES ON mydb.* TO 'alice'@'localhost';
```

To apply changes:
```sql
FLUSH PRIVILEGES;
```

To revoke privileges:
```sql
REVOKE privilege_type ON database.table FROM 'username'@'host';
```

## 3. What’s a PRIMARY KEY

A `PRIMARY KEY` uniquely identifies each row in a table. It must be unique and NOT NULL.

**Example:**
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);
```

## 4. What’s a FOREIGN KEY

A `FOREIGN KEY` enforces a link between the data in two tables, referencing the `PRIMARY KEY` of another table.

**Example:**
```sql
CREATE TABLE orders (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## 5. How to Use NOT NULL and UNIQUE Constraints

- `NOT NULL`: Ensures a column cannot have a NULL value.
- `UNIQUE`: Ensures all values in a column are different.

**Example:**
```sql
CREATE TABLE products (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);
```

## 6. How to Retrieve Data from Multiple Tables in One Request

Use `JOIN` to combine rows from two or more tables based on a related column.

**Example:**
```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

## 7. What are Subqueries

A subquery is a query nested inside another query.

**Example:**
```sql
SELECT name FROM users
WHERE id IN (SELECT user_id FROM orders WHERE price > 100);
```

## 8. What are JOIN and UNION

- `JOIN`: Combines rows from two or more tables based on a related column.
  - Types: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, etc.

- `UNION`: Combines results from two or more SELECT statements into a single result set. Each SELECT must have the same number of columns and compatible types.

**JOIN Example:**
```sql
SELECT users.name, orders.id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

**UNION Example:**
```sql
SELECT name FROM customers
UNION
SELECT name FROM suppliers;
```

---

## 9. What is an SQL Dump (Backup & Restore)

An SQL dump is a text file containing all the SQL statements needed to recreate a database's structure and data. It's commonly used for backups, migrations, or transferring databases between servers.

### How to Create an SQL Dump

Use the `mysqldump` command-line tool:

```bash
mysqldump -u username -p database_name > backup.sql
```
- `username`: your MySQL username
- `database_name`: the database to back up
- `backup.sql`: the output file

You will be prompted for your password.

### How to Restore an SQL Dump

To restore a database from a dump file:

```bash
mysql -u username -p database_name < backup.sql
```
- Make sure the target database (`database_name`) exists before running this command.

**Tip:** You can also dump only specific tables or add options for structure/data only. See `mysqldump --help` for more options.
