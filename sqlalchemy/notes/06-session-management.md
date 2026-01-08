# Session Management

## Understanding the Session

The Session is your gateway to the database:

1. **Identity Map** - Maintains unique instance of each object
2. **Unit of Work** - Tracks modifications and synchronizes changes
3. **Transaction Management** - Manages database transactions

## Creating Sessions

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()
```

## Session Lifecycle

```python
# 1. Create session
session = Session()

try:
    # 2. Add/modify objects
    new_user = User(name='Alice', email='alice@example.com')
    session.add(new_user)

    # 3. Commit transaction
    session.commit()
except:
    # 4. Rollback on error
    session.rollback()
    raise
finally:
    # 5. Close session
    session.close()
```

## Transaction Management

### Committing Changes

```python
session.add(user1)
session.add(user2)
session.commit()  # Writes changes to database
```

### Rolling Back

```python
try:
    session.add(user1)
    session.add(user2)
    session.commit()
except:
    session.rollback()  # Undo all changes
    raise
```

### Using Context Managers

```python
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

## Session Configuration

### Custom Session Settings

```python
Session = sessionmaker(
    bind=engine,
    autocommit=False,        # Explicit commits
    autoflush=False,         # Manual flushing
    expire_on_commit=False   # Objects don't expire after commit
)
```

### Flushing

Flush sends pending changes to database without committing:

```python
user = User(name='Alice')
session.add(user)
session.flush()  # Syncs to database, but transaction still open
print(user.id)   # ID is now available
session.commit() # Actually commits the transaction
```

## Handling Concurrency

### Optimistic Concurrency Control

```python
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

# Check for concurrent updates
user = session.query(User).filter_by(id=1).first()
old_updated_at = user.updated_at
user.name = 'New Name'
session.commit()

if user.updated_at != old_updated_at:
    print("Record was updated by another transaction!")
```

### Isolation Levels

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Set isolation level
connection = engine.connect()
connection = connection.execution_options(
    isolation_level="READ COMMITTED"
)
session = Session(bind=connection)
```

Common isolation levels:

- `READ UNCOMMITTED`
- `READ COMMITTED`
- `REPEATABLE READ`
- `SERIALIZABLE`

## Bulk Operations

### Bulk Insert

```python
session.bulk_save_objects([
    User(name='User1'),
    User(name='User2'),
    User(name='User3')
])
session.commit()
```

### Bulk Update

```python
session.bulk_update_mappings(User, [
    {'id': 1, 'name': 'Updated User1'},
    {'id': 2, 'name': 'Updated User2'}
])
session.commit()
```

## Session Binding

Bind session to multiple engines:

```python
engine1 = create_engine('sqlite:///db1.sqlite')
engine2 = create_engine('sqlite:///db2.sqlite')

Session = sessionmaker(binds={
    User: engine1,
    Address: engine2
})
```

## Best Practices

1. **Always close sessions** - Use context managers
2. **One session per request** - In web applications
3. **Keep sessions short-lived** - Don't hold open too long
4. **Use scoped sessions** - For thread-local sessions
5. **Handle exceptions properly** - Always rollback on errors

### Scoped Sessions (Thread-Local)

```python
from sqlalchemy.orm import scoped_session, sessionmaker

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Usage
session = Session()
# ... do work
Session.remove()  # Clean up
```

### Web Application Pattern

```python
# Flask example
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
engine = create_engine('sqlite:///app.db')
db_session = scoped_session(sessionmaker(bind=engine))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/users')
def get_users():
    users = db_session.query(User).all()
    return jsonify([u.name for u in users])
```
