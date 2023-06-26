import PySimpleGUI as sg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knygos.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()



class Base(DeclarativeBase):
    pass


Base.metadata.create_all(db_engine)


class Autoriai(Base):
    __tablename__ = 'Autoriai'
    id = mapped_column(Integer, primary_key=True)
    vardas = mapped_column(String(50), nullable=False)
    pavarde = mapped_column(String(50), nullable=False)


class Knygos(Base):
    __tablename__ = 'Knygos'
    id = mapped_column(Integer, primary_key=True)
    pavadinmas = mapped_column(String(50), nullable=False)
    leidimo_metai = mapped_column(Integer(50), nullable=False)

