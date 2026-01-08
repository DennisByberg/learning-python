# Advanced ORM Concepts

## Inheritance Mapping

### Single Table Inheritance

All classes in hierarchy stored in one table:

```python
from sqlalchemy import Column, Integer, String

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': type
    }

class Manager(Employee):
    department = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }

class Engineer(Employee):
    programming_language = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'engineer',
    }
```

### Joined Table Inheritance

Separate tables with foreign key relationships:

```python
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': type
    }

class Manager(Employee):
    __tablename__ = 'managers'

    id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    department = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'manager',
    }
```

## Hybrid Properties

Properties that work both in Python and SQL:

```python
from sqlalchemy.ext.hybrid import hybrid_property

class Rectangle(Base):
    __tablename__ = 'rectangles'

    id = Column(Integer, primary_key=True)
    width = Column(Integer)
    height = Column(Integer)

    @hybrid_property
    def area(self):
        return self.width * self.height

    @area.expression
    def area(cls):
        return cls.width * cls.height

# Usage
rectangles = session.query(Rectangle).filter(Rectangle.area > 100).all()
```

## Custom Types

Define custom column types:

```python
from sqlalchemy.types import TypeDecorator, VARCHAR
import json

class JSONEncodedDict(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    preferences = Column(JSONEncodedDict)
```

## Eager vs Lazy Loading

### Lazy Loading (Default)

Related objects loaded only when accessed:

```python
users = session.query(User).all()
for user in users:
    print(user.addresses)  # Triggers separate query for each user (N+1 problem!)
```

### Eager Loading Solutions

**1. Joined Loading**

```python
from sqlalchemy.orm import joinedload

users = session.query(User).options(joinedload(User.addresses)).all()
```

**2. Subquery Loading**

```python
from sqlalchemy.orm import subqueryload

users = session.query(User).options(subqueryload(User.addresses)).all()
```

**3. Selectin Loading**

```python
from sqlalchemy.orm import selectinload

users = session.query(User).options(selectinload(User.addresses)).all()
```

## Query Optimization

### Select Specific Columns

```python
# Instead of loading entire objects
users = session.query(User.id, User.name).all()
```

### Use Indexes

```python
from sqlalchemy import Index

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), index=True)  # Simple index
    name = Column(String(50))

    # Or create index separately
    __table_args__ = (
        Index('ix_user_email_name', 'email', 'name'),
    )
```

### Bulk Operations

```python
# Bulk insert
session.bulk_save_objects([
    User(name='User1'),
    User(name='User2'),
    User(name='User3')
])

# Bulk update
session.bulk_update_mappings(User, [
    {'id': 1, 'name': 'Updated User1'},
    {'id': 2, 'name': 'Updated User2'}
])
session.commit()
```

## Events and Listeners

React to database events:

```python
from sqlalchemy import event

@event.listens_for(User, 'before_insert')
def receive_before_insert(mapper, connection, target):
    print(f"New user being inserted: {target.name}")

@event.listens_for(User, 'after_update')
def receive_after_update(mapper, connection, target):
    print(f"User updated: {target.name}")
```

## Hybrid Expressions

```python
from sqlalchemy.ext.hybrid import hybrid_method

class Interval(Base):
    __tablename__ = 'intervals'

    id = Column(Integer, primary_key=True)
    start = Column(Integer)
    end = Column(Integer)

    @hybrid_method
    def contains(self, point):
        return (self.start <= point) & (point < self.end)

    @contains.expression
    def contains(cls, point):
        return (cls.start <= point) & (point < cls.end)

# Usage
intervals = session.query(Interval).filter(Interval.contains(15)).all()
```
