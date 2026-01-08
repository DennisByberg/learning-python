"""
Exercise 9: Query with Relationships
====================================
Learn how to query data across related tables.
Why this exercise?
------------------
Nu använder du relationerna du skapade! user.addresses ger dig automatiskt alla
relaterade addresses - SQLAlchemy kör JOIN SQL i bakgrunden.
Detta är otroligt kraftfullt eftersom du kan navigera mellan objekt som vanliga
Python-attribut, utan att skriva komplexa JOIN queries. Koden blir ren och läsbar!"""

from sqlalchemy import String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)

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

    addresses: Mapped[list["Address"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', age={self.age})"


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(String(120))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id}, email_address='{self.email_address}', user_id={self.user_id})"


if __name__ == "__main__":
    print("Exercise 9: Query with Relationships")
    print("=" * 50)

    # TODO: Create a session
    # Why? Always need a session for queries.
    Session = sessionmaker(bind=engine)
    session = Session()

    # TODO: Query all users
    # TODO: For each user, print username and their addresses
    # Why? user.addresses is automatically populated by SQLAlchemy!
    # No JOIN SQL needed - just access the attribute like any Python list.
    # Hint: Use user.addresses to access related addresses

    print("\n--- Users and their addresses ---")
    # Your code here

    # TODO: Query all addresses
    # TODO: For each address, print email_address and the username it belongs to
    # Why? Works in reverse too! address.user gives you the related User object.
    # This is the power of back_populates - bidirectional navigation.
    # Hint: Use address.user.username

    print("\n--- Addresses and their users ---")
    # Your code here

    # TODO: Close the session
    # Why? Clean up resources!
