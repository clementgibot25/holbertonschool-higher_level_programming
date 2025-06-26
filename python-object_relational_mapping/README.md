# Python Object Relational Mapping (ORM) and MySQL

This project demonstrates how to interact with a MySQL database using Python, both with direct SQL queries and with an Object Relational Mapper (ORM) such as SQLAlchemy.

## MySQLdb

[MySQLdb](https://mysqlclient.readthedocs.io/) is a Python library that allows you to connect to and interact with a MySQL database using SQL queries directly.

### Connecting to MySQL with MySQLdb
```python
import MySQLdb

# Establish a database connection
db = MySQLdb.connect(
    host="localhost",
    user="your_username",
    passwd="your_password",
    db="your_database"
)
# Create a cursor to execute SQL queries
cursor = db.cursor()
# The cursor is used to execute SQL commands and fetch results
# It's essential for interacting with the database
```

### SELECT rows with MySQLdb
```python
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

### INSERT rows with MySQLdb
```python
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@email.com"))
db.commit()
```

---

## SQLAlchemy

[SQLAlchemy](https://www.sqlalchemy.org/) is a popular Python SQL toolkit and ORM. It allows you to use Python classes to represent database tables and provides a high-level, Pythonic interface to interact with your database.

### What is an ORM?
**ORM** stands for **Object Relational Mapper**. It is a programming technique that lets you interact with your database using objects (Python classes) instead of writing raw SQL queries. This makes code easier to write, read, and maintain.

### Connecting to MySQL with SQLAlchemy
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://your_username:your_password@localhost/your_database')
Session = sessionmaker(bind=engine)
session = Session()
```

### Mapping a Python Class to a MySQL Table
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
```

### SELECT rows with SQLAlchemy
```python
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email)
```

### INSERT rows with SQLAlchemy
```python
new_user = User(name="Bob", email="bob@email.com")
session.add(new_user)
session.commit()
```

---

## Summary Table
| Feature         | MySQLdb (Raw SQL)             | SQLAlchemy (ORM)         |
|-----------------|------------------------------|--------------------------|
| Connection      | Manual (MySQLdb.connect)      | Engine (create_engine)   |
| SELECT          | cursor.execute + fetchall     | session.query            |
| INSERT          | cursor.execute + commit       | session.add + commit     |
| Mapping         | Manual                        | Python classes           |
| Abstraction     | Low (SQL strings)             | High (Python objects)    |

---

## References
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)

---
