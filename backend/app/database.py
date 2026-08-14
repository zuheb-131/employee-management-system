from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. PostgreSQL Database URL Configuration
# Format: postgresql://<username>:<password>@<host>:<port>/<database_name>
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Zuheb123@localhost:5432/employee_db"

# 2. Create SQLAlchemy Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Create SessionLocal class for DB operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create Base class for DB models
Base = declarative_base()

# 5. Dependency to get DB session in FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()