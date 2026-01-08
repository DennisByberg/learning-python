# Asynchronous SQLAlchemy

## Introduction to Async

Async SQLAlchemy allows non-blocking database operations, perfect for:

- High-concurrency applications
- FastAPI and other async frameworks
- I/O-bound operations

## Installation

```bash
pip install sqlalchemy[asyncio]

# PostgreSQL async driver
pip install asyncpg

# MySQL async driver
pip install aiomysql

# SQLite async driver
pip install aiosqlite
```

## Setup Async Engine

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Create async engine
engine = create_async_engine(
    "postgresql+asyncpg://user:password@localhost/dbname",
    echo=True
)

# Create async session
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
```

## Defining Models

Models are defined the same way as synchronous:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
```

## CRUD Operations

### Create

```python
async def create_user(name: str, email: str):
    async with async_session() as session:
        new_user = User(name=name, email=email)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

# Usage
import asyncio

async def main():
    user = await create_user("Alice", "alice@example.com")
    print(f"Created user: {user.name}")

asyncio.run(main())
```

### Read

```python
from sqlalchemy import select

async def get_user(user_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

# Usage
async def main():
    user = await get_user(1)
    if user:
        print(f"Found user: {user.name}")
    else:
        print("User not found")

asyncio.run(main())
```

### Update

```python
async def update_user_email(user_id: int, new_email: str):
    async with async_session() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            user.email = new_email
            await session.commit()
            return user
        return None

# Usage
async def main():
    user = await update_user_email(1, "new_alice@example.com")
    if user:
        print(f"Updated: {user.email}")

asyncio.run(main())
```

### Delete

```python
async def delete_user(user_id: int):
    async with async_session() as session:
        stmt = select(User).where(User.id == user_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()

        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False

# Usage
async def main():
    deleted = await delete_user(1)
    print(f"Deleted: {deleted}")

asyncio.run(main())
```

## Querying

### Basic Queries

```python
async def get_all_users():
    async with async_session() as session:
        stmt = select(User)
        result = await session.execute(stmt)
        return result.scalars().all()
```

### With Filters

```python
async def get_users_by_email_domain(domain: str):
    async with async_session() as session:
        stmt = select(User).where(User.email.like(f"%@{domain}"))
        result = await session.execute(stmt)
        return result.scalars().all()
```

### With Joins

```python
async def get_users_with_addresses():
    async with async_session() as session:
        stmt = select(User).join(Address).where(Address.email.like("%gmail%"))
        result = await session.execute(stmt)
        return result.scalars().all()
```

### Eager Loading

```python
from sqlalchemy.orm import selectinload

async def get_users_with_addresses_eager():
    async with async_session() as session:
        stmt = select(User).options(selectinload(User.addresses))
        result = await session.execute(stmt)
        return result.scalars().all()
```

## FastAPI Integration

```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

app = FastAPI()

# Dependency
async def get_db():
    async with async_session() as session:
        yield session

# Pydantic models
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Routes
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.get("/users/", response_model=List[UserResponse])
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

## Best Practices

### 1. Use async with

Always use context managers:

```python
async with async_session() as session:
    # Your operations
    await session.commit()
```

### 2. Error Handling

```python
from sqlalchemy.exc import SQLAlchemyError

async def safe_create_user(name: str, email: str):
    try:
        async with async_session() as session:
            new_user = User(name=name, email=email)
            session.add(new_user)
            await session.commit()
            return new_user
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        return None
```

### 3. Pagination

```python
async def get_users_paginated(page: int, per_page: int):
    async with async_session() as session:
        stmt = select(User).limit(per_page).offset((page - 1) * per_page)
        result = await session.execute(stmt)
        return result.scalars().all()
```

### 4. Connection Pooling

```python
engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/dbname",
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True  # Verify connections before using
)
```

### 5. Don't Mix Sync and Async

```python
# BAD - Don't do this
async def bad_example():
    user = session.query(User).first()  # Sync call in async function!

# GOOD
async def good_example():
    async with async_session() as session:
        result = await session.execute(select(User))
        user = result.scalar_one_or_none()
```

## Performance Considerations

### Concurrent Operations

```python
async def process_multiple_users():
    tasks = [
        create_user("User1", "user1@example.com"),
        create_user("User2", "user2@example.com"),
        create_user("User3", "user3@example.com"),
    ]

    users = await asyncio.gather(*tasks)
    return users
```

### Batch Operations

```python
async def bulk_create_users(user_list: List[dict]):
    async with async_session() as session:
        users = [User(**user_data) for user_data in user_list]
        session.add_all(users)
        await session.commit()
```
