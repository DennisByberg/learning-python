# Introduction to SQLAlchemy

## What is SQLAlchemy?

SQLAlchemy is an open-source SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a full suite of enterprise-level persistence patterns designed for efficient and high-performing database access.

## Why Use ORMs?

**Object-Relational Mapping (ORM)** tools bridge the gap between object-oriented programming and relational databases:

1. **Abstraction** - Work with familiar OOP paradigms instead of raw SQL
2. **Productivity** - Eliminate need to write SQL for most operations
3. **Portability** - Support multiple database backends easily
4. **Security** - Built-in protection against SQL injection
5. **Maintainability** - More readable and maintainable code

## Core vs ORM

SQLAlchemy consists of two main components:

### SQLAlchemy Core

- **Foundational layer** providing SQL abstraction
- **SQL Expression Language** - Pythonic way of writing SQL
- **Fine-grained control** over generated queries
- **Closer to SQL** - ideal for performance-critical operations

### SQLAlchemy ORM

- **Built on top of Core** with higher-level abstraction
- **Maps Python classes** to database tables
- **Automates** common database operations
- **Pythonic approach** - ideal for rapid development

## Key Features

1. **Database Agnostic** - PostgreSQL, MySQL, SQLite, Oracle, MS SQL Server
2. **Powerful Query Construction** - Complex joins, subqueries, unions
3. **Connection Pooling** - Efficient connection management
4. **Transaction Management** - Robust transaction control
5. **Schema Management** - Create and modify database schemas
6. **Relationship Management** - one-to-many, many-to-many support
7. **Type Annotations** (2.0+) - Enhanced IDE support
8. **Async Support** (2.0+) - Native async/await functionality

## Resources

- [Official Documentation](https://docs.sqlalchemy.org/)
- [Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- Article: [Mastering SQLAlchemy](https://medium.com/@ramanbazhanau/mastering-sqlalchemy-a-comprehensive-guide-for-python-developers-ddb3d9f2e829)
