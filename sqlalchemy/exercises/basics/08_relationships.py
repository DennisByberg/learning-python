"""
Exercise 8: One-to-Many Relationship
====================================
Learn how to create relationships between models.
Why this exercise?
------------------
Riktiga applikationer har alltid relationer mellan tabeller! En user har många addresses,
en blogg har många posts, etc. ForeignKey kopplar tabellerna i databasen, medan
relationship() ger dig Python-attribut för att navigera mellan dem.
back_populates synkar automatiskt båda sidorna - när du lägger till en address
till user.addresses, sätts address.user automatiskt. Super smidigt!"""

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

    # Relationship to Address
    addresses: Mapped[list["Address"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}', age={self.age})"


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email_address: Mapped[str] = mapped_column(String(120))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # Relationship to User
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id}, email_address='{self.email_address}', user_id={self.user_id})"


# Create tables
Base.metadata.create_all(engine)

if __name__ == "__main__":
    print("Exercise 8: One-to-Many Relationship")
    print("=" * 50)

    # TODO: Create a session
    # Why? You know this by now!
    Session = sessionmaker(bind=engine)
    session = Session()

    # TODO: Find or create user 'Alice'
    # Why? We need an existing user to attach addresses to. If Alice doesn't exist,
    # create her first so we have someone to link addresses to.
    # Hint: session.query(User).filter_by(username="Alice").first()

    # TODO: Create 2 addresses for Alice
    # Why? This demonstrates one-to-many: one user, many addresses.
    # The user=alice parameter automatically sets the foreign key!
    #       - alice@work.com
    #       - alice@home.com
    # Hint: Address(email_address="...", user=alice)

    # TODO: Add addresses to session
    # Why? Stage the new addresses for insertion into the database.

    # TODO: Commit the changes
    # Why? Save addresses to database. SQLAlchemy handles the foreign key relationship.

    # TODO: Print Alice and her addresses
    # Why? See the relationship in action! alice.addresses is a list you can loop through.

    # TODO: Close the session
    # Why? Clean up!
