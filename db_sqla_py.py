from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, sessionmaker
from typing import Any

engine = create_engine('sqlite:///seima.db')
session = sessionmaker(bind=engine)()


class Base(DeclarativeBase):
    pass

class Tevas(Base):
    __tablename__ = "tevas"
    id = mapped_column(Integer, primary_key=True)
    vardas = mapped_column("vardas", String(50))
    pavarde = mapped_column("pavarde", String(50))
    vaikai = relationship("Vaikas", back_populates="tevas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = mapped_column(Integer, primary_key=True)
    vardas = mapped_column("vardas", String(50))
    pavarde = mapped_column("pavarde", String(50))
    mokykla = mapped_column("mokykla", String(50))
    tevas_id = mapped_column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas", back_populates="vaikai")


Base.metadata.create_all(engine)

kestutis = Tevas(vardas="Kestutis", pavarde="J")
emilija = Vaikas(vardas="Emilija", pavarde="J", mokykla="gera", tevas=kestutis)
maja = Vaikas(vardas="Maja", pavarde="J")
marco = Vaikas(vardas="Marco", pavarde="J")
kestutis.vaikai.append(maja)
marco.tevas = kestutis
session.add_all([kestutis, emilija, maja, marco])
session.commit()

tevas = session.query(Tevas).first()
print(tevas.vardas)