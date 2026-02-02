from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MYSQL_USER="root"
MYSQL_PASSWORD="password"
MYSQL_HOST="localhost"
MYSQL_PORT="3306"
MYSQL_DB="mydatabase"

DATABASE_URL = f"mysql+pymysql://root:Vivek%402437 @localhost:3306/testdb"

engine = create_engine(DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)      

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base() 