# Migrations with Alembic

## What is Alembic?

Alembic is a lightweight database migration tool for SQLAlchemy. It provides version control for your database schema.

## Installation

```bash
pip install alembic
```

## Initialize Alembic

```bash
alembic init alembic
```

This creates:

- `alembic/` directory with migration environment
- `alembic.ini` configuration file

## Configuration

### Update alembic.ini

```ini
sqlalchemy.url = postgresql://username:password@localhost/dbname
```

### Update env.py

```python
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from your_app import models
from your_app.database import Base

target_metadata = Base.metadata
```

## Creating Migrations

### Auto-generate Migration

```bash
alembic revision --autogenerate -m "Create users table"
```

### Manual Migration

```bash
alembic revision -m "Add email column"
```

### Migration Example

```python
"""Add email column

Revision ID: abc123def456
Revises: previous_revision
Create Date: 2025-01-07 12:00:00.000000
"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers
revision = 'abc123def456'
down_revision = 'previous_revision'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users',
        sa.Column('email', sa.String(120), nullable=True)
    )

def downgrade():
    op.drop_column('users', 'email')
```

## Applying Migrations

### Upgrade to Latest

```bash
alembic upgrade head
```

### Upgrade to Specific Version

```bash
alembic upgrade abc123def456
```

### Downgrade

```bash
# Downgrade one revision
alembic downgrade -1

# Downgrade to specific revision
alembic downgrade abc123def456

# Downgrade all
alembic downgrade base
```

## Migration Operations

### Creating Tables

```python
def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(120), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
```

### Adding Columns

```python
def upgrade():
    op.add_column('users',
        sa.Column('age', sa.Integer(), nullable=True)
    )
```

### Dropping Columns

```python
def upgrade():
    op.drop_column('users', 'age')
```

### Altering Columns

```python
def upgrade():
    op.alter_column('users', 'email',
        existing_type=sa.String(50),
        type_=sa.String(120),
        nullable=False
    )
```

### Creating Indexes

```python
def upgrade():
    op.create_index('ix_users_email', 'users', ['email'])
```

### Adding Foreign Keys

```python
def upgrade():
    op.create_foreign_key(
        'fk_address_user',
        'addresses', 'users',
        ['user_id'], ['id']
    )
```

## Data Migrations

Migrate data while changing schema:

```python
from sqlalchemy.sql import table, column

def upgrade():
    users = table('users',
        column('id', sa.Integer),
        column('name', sa.String),
        column('full_name', sa.String)
    )

    # Add new column
    op.add_column('users', sa.Column('full_name', sa.String(100)))

    # Migrate data
    op.execute(users.update().values(full_name=users.c.name))

    # Drop old column
    op.drop_column('users', 'name')
```

## Batch Operations

For large tables or SQLite:

```python
from alembic import op

def upgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('name',
            existing_type=sa.String(50),
            type_=sa.String(100)
        )
```

## Best Practices

### 1. Incremental Changes

Make small, focused migrations:

```python
# Good: One change per migration
def upgrade():
    op.add_column('users', sa.Column('age', sa.Integer()))
```

### 2. Always Test Migrations

```python
# Test both upgrade and downgrade
alembic upgrade head
alembic downgrade -1
alembic upgrade head
```

### 3. Version Control

Always commit migrations to version control:

```bash
git add alembic/versions/
git commit -m "Add user email migration"
```

### 4. Never Edit Applied Migrations

If migration is already applied, create new migration to fix issues.

### 5. Use Descriptive Messages

```bash
alembic revision --autogenerate -m "Add user authentication fields"
```

## Checking Migration Status

```bash
# View current status
alembic current

# View migration history
alembic history

# View specific revision
alembic show abc123def456
```

## Working with Branches

For feature branches:

```bash
# Create branch
alembic revision --branch-label feature_x -m "Start feature X"

# Merge branches
alembic merge -m "Merge feature X" branch1 branch2
```

## Example: Complete Migration Workflow

```bash
# 1. Initialize Alembic
alembic init alembic

# 2. Configure database URL in alembic.ini
# sqlalchemy.url = postgresql://user:pass@localhost/mydb

# 3. Create initial migration
alembic revision --autogenerate -m "Initial schema"

# 4. Review generated migration file
# (check alembic/versions/*.py)

# 5. Apply migration
alembic upgrade head

# 6. Make model changes in your code
# (modify SQLAlchemy models)

# 7. Generate new migration
alembic revision --autogenerate -m "Add user roles"

# 8. Apply new migration
alembic upgrade head
```
