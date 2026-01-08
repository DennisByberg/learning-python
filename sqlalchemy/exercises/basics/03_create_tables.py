"""
Exercise 3: Create Tables
=========================
Learn how to create database tables from your models.
Why this exercise?
------------------
Nu tar vi Python-modellerna och gör dem till riktiga databastabeller!
Base.metadata.create_all() läser alla dina modeller och skapar motsvarande
tabeller i databasen. Detta är otroligt kraftfullt - du slipper skriva CREATE TABLE
SQL-statements manuellt. SQLAlchemy översätter din Python-kod till rätt SQL för
vilken databas du än använder (SQLite, PostgreSQL, MySQL, etc.)."""

from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Create engine
engine = create_engine("sqlite:///basics.db")


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    age: Mapped[int | None] = mapped_column(Integer, nullable=True)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', age={self.age})"


if __name__ == "__main__":
    print("Exercise 3: Create Tables")
    print("=" * 50)

    # TODO: Use Base.metadata.create_all(engine) to create tables
    # Why? This single line creates ALL tables defined in your models.
    # It's safe to run multiple times - it won't recreate existing tables.

    # TODO: Print a success message
    # Why? Always confirm operations succeeded. Good for debugging and user feedback.

    # TODO: Print created table names
    # Why? Verify which tables were created. Useful when you have multiple models.
    # Hint: list(Base.metadata.tables.keys())
