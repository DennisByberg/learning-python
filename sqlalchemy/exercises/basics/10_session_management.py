"""
Exercise 10: Session Best Practices
===================================
Learn proper session management with context managers.
Why this exercise?
------------------
Context managers (@contextmanager och 'with') är BEST PRACTICE för sessions!
De garanterar att sessionen alltid stängs, även om något går fel.
Om ett fel uppstår, rullas alla ändringar tillbaka (rollback) automatiskt.
Om allt går bra, commit:as ändringarna. Detta förhindrar databasläckor och
korrupt data. I produktion ska du ALLTID använda denna pattern!"""

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


# Create Session class
Session = sessionmaker(bind=engine)


# TODO: Create a session_scope() context manager that:
# Why? This is the professional way to handle sessions! The try/except/finally
# ensures proper cleanup no matter what happens. If an error occurs, rollback
# prevents partial/corrupt data. If success, commit saves everything.
#       - Creates a new session
#       - Yields the session
#       - Commits on success
#       - Rolls back on error
#       - Always closes the session
#
# Hint:
# @contextmanager
# def session_scope():
#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except Exception:
#         session.rollback()
#         raise
#     finally:
#         session.close()


if __name__ == "__main__":
    print("Exercise 10: Session Best Practices")
    print("=" * 50)

    # TODO: Use the context manager to add a new user
    # Why? 'with' automatically handles commit/rollback/close!
    # The session is only open inside the 'with' block - automatic cleanup.
    # Hint:
    # with session_scope() as session:
    #     user = User(...)
    #     session.add(user)

    print("\n--- Add user successfully ---")
    # Your code here

    # TODO: Test error handling by trying to add a user with duplicate email
    # Why? See rollback in action! When an error occurs, the transaction is
    # automatically rolled back - no corrupt data in the database.
    # Hint: Wrap in try/except to catch the error

    print("\n--- Test duplicate email (should fail) ---")
    # Your code here
