"""
Exercise 6: Update Data
=======================
Learn how to modify existing records.
Why this exercise?
------------------
Uppdatering är 'U' i CRUD. Här ser du SQLAlchemy:s magi på riktigt!
Du hämtar ett objekt, ändrar dess attribut (som vanliga Python-properties),
och när du commit:ar så trackar SQLAlchemy vad som ändrats och genererar
rätt UPDATE SQL automatiskt. Ingen manuell SQL - bara Python!"""

from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

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
    print("Exercise 6: Update Data")
    print("=" * 50)

    # TODO: Create a session
    # Why? Always need a session for database operations.
    Session = sessionmaker(bind=engine)
    session = Session()

    # TODO: Find user 'Alice'
    # Why? You need to fetch the object before you can modify it.
    # Hint: session.query(User).filter_by(username="Alice").first()

    # TODO: Check if Alice exists
    # Why? Always validate before modifying! If .first() returns None, you'll get an error.

    # TODO: Update her email to 'alice.updated@example.com'
    # Why? Just change the attribute like any Python object! SQLAlchemy tracks the change.

    # TODO: Update her age to 26
    # Why? You can update multiple attributes. All changes are tracked until commit.

    # TODO: Commit the changes
    # Why? Nothing is saved until you commit. SQLAlchemy generates UPDATE SQL now.

    # TODO: Query Alice again to verify the changes
    # Why? Always verify updates worked. Good practice for testing and debugging.

    # TODO: Print the updated user
    # Why? Show the results to confirm everything looks correct.

    # TODO: Close the session
    # Why? Clean up resources!
