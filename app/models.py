from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer)
    genre = Column(String)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', year={self.year}, genre='{self.genre}')>"

if __name__ == "__main__":
    engine = create_engine("sqlite:///../biblioteca.db")  # Ajusta la ruta si es necesario
    Base.metadata.create_all(bind=engine)