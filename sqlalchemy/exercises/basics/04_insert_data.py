"""
Exercise 4: Insert Data (Create)
================================
Learn how to add new records to the database.
Why this exercise?
------------------
Nu börjar det bli riktigt kul! Sessions är ditt verktyg för att prata med databasen.
Du skapar Python-objekt (User-instanser) och lägger till dem i sessionen.
När du commit:ar, översätts allt till INSERT SQL-statements.
Detta är 'C' i CRUD (Create, Read, Update, Delete) - grunden för all datahantering."""

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


# Ensure tables exist
Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Exercise 4: Insert Data")
    print("=" * 50)

    # TODO: Create a Session class bound to the engine
    # Why? Session is a factory that creates connections to your database.
    # You bind it once to the engine, then use it to create individual sessions.
    # Hint: Session = sessionmaker(bind=engine)

    # TODO: Create a session instance
    # Why? Each session represents a "workspace" for database operations.
    # Think of it as a transaction - changes are tracked until you commit.

    # TODO: Create 3 users:
    # Why? Creating User objects is just Python - they're not in the DB yet!
    # They become database rows only after session.add() and session.commit().
    #       - Alice, alice@example.com, age 25
    #       - Bob, bob@example.com, age 30
    #       - Charlie, charlie@example.com, age 28

    # TODO: Add all users to the session
    # Why? session.add_all() stages objects for insertion. They're not in the DB yet,
    # just marked as "pending". You can still modify them before committing.
    # Hint: session.add_all([user1, user2, user3])

    # TODO: Commit the session
    # Why? Commit writes all changes to the database. Before this, everything is temporary.
    # If an error occurs before commit, nothing is saved - the database stays unchanged.

    # TODO: Print success message
    # Why? Confirm data was inserted. Good practice for user feedback.

    # TODO: Close the session
    # Why? Always close sessions to free database connections. Unclosed sessions can
    # cause connection leaks and slow down your app.
