import os
from sqlalchemy import create_engine
from models import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "biblioteca.db")
engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(bind=engine)