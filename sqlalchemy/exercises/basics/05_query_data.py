"""
Exercise 5: Query Data (Read)
=============================
Learn different ways to query and filter data.
Why this exercise?
------------------
Querying är det du kommer göra MEST! Detta är 'R' i CRUD.
Istället för att skriva SELECT SQL, använder du Python-metoder som .filter_by(),
.where(), och .like(). Det är typesäkert, lätt att läsa, och IDE:n kan hjälpa dig.
Du lär dig också skillnaden mellan .first() (ett resultat) och .all() (alla resultat)."""

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
    print("Exercise 5: Query Data")
    print("=" * 50)

    # TODO: Create a session
    # Why? You always need a session to query the database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # TODO: Query and print all users
    # Why? .all() returns a list of all User objects. Perfect when you need everything.
    # Hint: session.query(User).all()

    # TODO: Find and print user with username 'Alice'
    # Why? .filter_by() is simple for exact matches. .first() gets one result (or None).
    # Hint: session.query(User).filter_by(username="Alice").first()

    # TODO: Find and print all users older than 27
    # Why? .where() is powerful for comparisons (>, <, >=, etc). More flexible than filter_by.
    # Hint: session.query(User).where(User.age > 27).all()

    # TODO: Find and print users whose email contains 'example.com'
    # Why? .like() is for pattern matching (similar to SQL LIKE). Great for searches.
    # Hint: session.query(User).where(User.email.like("%example.com%")).all()

    # TODO: Close the session
    # Why? Always close to free resources!
