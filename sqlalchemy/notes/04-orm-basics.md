# SQLAlchemy ORM Basics

## Defining Models

### Basic Model Definition

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create database tables
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)
```

### SQLAlchemy 2.0 Style with Type Hints

```python
from typing import List
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120))
```

## Relationships

### One-to-Many

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(120), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
```

### Many-to-Many

```python
from sqlalchemy import Table

# Association table
student_course = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    students = relationship("Student", secondary=student_course, back_populates="courses")
```

## CRUD Operations

### Create (Insert)

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Create new user
new_user = User(name='Alice', email='alice@example.com')
session.add(new_user)
session.commit()
```

### Read (Select)

```python
# Fetch all users
users = session.query(User).all()

# Fetch specific user
user = session.query(User).filter_by(name='Alice').first()

# Filter with conditions
users = session.query(User).filter(User.name.like('A%')).all()
```

### Update

```python
user = session.query(User).filter_by(name='Alice').first()
user.email = 'alice_new@example.com'
session.commit()
```

### Delete

```python
user = session.query(User).filter_by(name='Alice').first()
session.delete(user)
session.commit()
```

## Querying with ORM

### Basic Queries

```python
# All users
users = session.query(User).all()

# Filter
users = session.query(User).filter_by(name='Alice').all()

# Like operator
users = session.query(User).filter(User.name.like('Al%')).all()
```

### Ordering

```python
users = session.query(User).order_by(User.name).all()
```

### Limiting

```python
users = session.query(User).limit(5).all()
```

### Joins

```python
results = session.query(User, Address).join(Address).all()
```

### Aggregations

```python
from sqlalchemy import func

# Count users
user_count = session.query(func.count(User.id)).scalar()

# Group by
results = session.query(
    User.name,
    func.count(Address.id).label('address_count')
).join(Address).group_by(User.name).all()
```

## Session Best Practices

Always close sessions properly:

```python
# Using context manager (recommended)
from contextlib import contextmanager

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# Usage
with session_scope() as session:
    user = User(name='Bob')
    session.add(user)
```
