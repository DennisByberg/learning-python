"""
Exercise 2: Define Your First Model
===================================
Create a User model with basic fields.

Why this exercise?
------------------
Models are the heart of SQLAlchemy! They define your table structure using Python code.
Instead of writing SQL directly, you use Python classes that represent tables.
This makes your code more readable, type-safe, and easier to maintain. When you change
the model, the table changes - no manual SQL needed!
"""

from sqlalchemy import create_engine

# Create engine
engine = create_engine("sqlite:///basics.db")

# TODO: Create Base class using DeclarativeBase
# Why? Base is the foundation all your models inherit from. It tracks all models
# and provides the metadata needed to create tables.
# Hint: class Base(DeclarativeBase): pass


# TODO: Define User class with:
# Why? This Python class becomes a database table. Each attribute becomes a column.
# SQLAlchemy uses type hints (Mapped) to understand column types and generate correct SQL.
#       - __tablename__ = 'users'
#       - id (Integer, primary_key, autoincrement)
#       - username (String(50), not nullable, unique)
#       - email (String(120), not nullable, unique)
#       - age (Integer, nullable)


# TODO: Add __repr__ method to print user info nicely
# Why? Without __repr__, printing a User object shows ugly memory address.
# With it, you get readable output like "User(id=1, username='Alice')" - great for debugging!
# Hint: return f"User(id={self.id}, username='{self.username}'...)"


if __name__ == "__main__":
    print("Exercise 2: Define Your First Model")
    print("=" * 50)

    # Your code here:
    pass
