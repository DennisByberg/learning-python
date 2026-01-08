"""
Exercise 7: Delete Data
=======================
Learn how to remove records from the database.
Why this exercise?
------------------
Detta är 'D' i CRUD - sista pusselbiten! session.delete() markerar objektet
för borttagning, och vid commit körs DELETE SQL. Viktigt att alltid kolla
om objektet finns först (if user:) innan delete, annars får du fel.
Nu kan du alla grundläggande databasoperationer!"""

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
    print("Exercise 7: Delete Data")
    print("=" * 50)

    # TODO: Create a session
    # Why? You know the drill by now!
    Session = sessionmaker(bind=engine)
    session = Session()

    # TODO: Find user 'Charlie'
    # Why? Must fetch the object before you can delete it.
    # Hint: session.query(User).filter_by(username="Charlie").first()

    # TODO: Check if Charlie exists
    # Why? Trying to delete None will crash! Always check first.

    # TODO: If found, delete Charlie using session.delete()
    # Why? session.delete() marks object for deletion. It's staged, not deleted yet.

    # TODO: Commit the changes
    # Why? The DELETE SQL runs now. Before commit, Charlie is still in the database.

    # TODO: Print success or not found message
    # Why? Give feedback! User should know if the operation succeeded or not.

    # TODO: Verify deletion by querying all users
    # Why? Confirm Charlie is really gone. Good for learning and testing.

    # TODO: Close the session
    # Why? Always clean up!
