from sqlalchemy import create_engine, text

"""
Exercise 1: Setup and First Connection
======================================
Learn how to create a database connection and test it.
"""


if __name__ == "__main__":
    print("Exercise 1: Setup and First Connection")
    print("=" * 50)

    # 1. Create an engine for SQLite database 'basics.db'
    engine = create_engine("sqlite:///basics.db")

    # 2. Test the connection by executing a simple query
    with engine.connect() as conn:
        result = conn.execute(text("SELECT sqlite_version()"))
        # 3. Print SQLite version
        print(f"SQLite version: {result.scalar()}")
