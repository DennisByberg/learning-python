# SQLAlchemy Core Concepts

## The Expression Language

SQLAlchemy Core provides a SQL abstraction layer using Python constructs.

### Table and Column Definitions

```python
from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)
```

### SQL Expressions

```python
from sqlalchemy import select

# SELECT * FROM users
stmt = select(users)

# SELECT name, email FROM users WHERE name = 'Alice'
stmt = select(users.c.name, users.c.email).where(users.c.name == 'Alice')
```

### Joins

```python
addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('email_address', String)
)

# JOIN users and addresses
stmt = select(users, addresses).join(
    addresses,
    users.c.id == addresses.c.user_id
)
```

### Ordering and Grouping

```python
from sqlalchemy import desc, func

# ORDER BY
stmt = select(users).order_by(desc(users.c.name))

# GROUP BY
stmt = select(
    users.c.name,
    func.count(addresses.c.id)
).join(addresses).group_by(users.c.name)
```

## Executing Queries

### Using execute()

```python
from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///example.db')

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM users WHERE name=:name"),
        {"name": "Alice"}
    )
    for row in result:
        print(row)
```

### Insert Operations

```python
from sqlalchemy import insert

stmt = insert(users).values(name='Bob', email='bob@example.com')

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
```

### Update Operations

```python
from sqlalchemy import update

stmt = update(users).where(
    users.c.name == 'Bob'
).values(email='bob_new@example.com')

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
```

### Delete Operations

```python
from sqlalchemy import delete

stmt = delete(users).where(users.c.name == 'Bob')

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
```

## Transactions

```python
# Auto-commit on success
with engine.begin() as conn:
    conn.execute(insert(users).values(name='Charlie', email='charlie@example.com'))
    conn.execute(insert(users).values(name='Diana', email='diana@example.com'))
    # Automatically commits if no exceptions
```

## Schema Management

### Creating Tables

```python
metadata.create_all(engine)
```

### Reflecting Existing Tables

```python
metadata = MetaData()
users = Table('users', metadata, autoload_with=engine)
```

### Altering Tables

```python
from sqlalchemy import Column, String

def upgrade(engine):
    meta = MetaData(bind=engine)
    users = Table('users', meta, autoload=True)
    new_column = Column('phone', String(15))
    new_column.create(users)
```

## When to Use Core vs ORM

**Use Core when:**

- Need maximum performance
- Writing complex queries
- Working on data migration scripts
- Require fine-grained SQL control

**Use ORM when:**

- Building applications with business logic
- Need object-oriented data models
- Want automated relationship handling
- Rapid application development
