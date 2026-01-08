# Setup and Installation

## Installation

### Basic Installation

```bash
pip install sqlalchemy
```

### Specific Version (2.0)

```bash
pip install sqlalchemy==2.0.0
```

### With Async Support

```bash
pip install sqlalchemy[asyncio]
```

## Database Drivers

Different databases require specific drivers:

### PostgreSQL

```bash
pip install psycopg2
# Or async driver
pip install asyncpg
```

### MySQL

```bash
pip install mysqlclient
```

### SQLite

No additional installation needed - included with Python!

## Virtual Environment Setup

Always use virtual environments for isolation:

```bash
# Create virtual environment
python -m venv sqlalchemy_env

# Activate (Linux/Mac)
source sqlalchemy_env/bin/activate

# Activate (Windows)
sqlalchemy_env\Scripts\activate
```

## Verify Installation

```python
import sqlalchemy
print(sqlalchemy.__version__)
```

## Connection Strings

### SQLite (Development)

```python
engine = create_engine('sqlite:///example.db')
```

### PostgreSQL

```python
engine = create_engine('postgresql://username:password@localhost:5432/dbname')
```

### MySQL

```python
engine = create_engine('mysql://username:password@localhost/dbname')
```

## First SQLAlchemy Program

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine('sqlite:///example.db')

# Create base class
Base = declarative_base()

# Define model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add a user
new_user = User(name='Alice', email='alice@example.com')
session.add(new_user)
session.commit()

# Query
user = session.query(User).filter_by(name='Alice').first()
print(user)

session.close()
```
