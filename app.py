from sqlalchemy import create_engine, Column, String,  Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship 

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column("id", Integer, primary_key = True)
    username = Column("username", String, unique = True)
       
#engine = create_engine('sqlite:///:memory:',echo=True)
engine = create_engine('sqlite:///person.db',echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
#person = Person()
#person.id = 0
#person.username = "Thulasi"
#session.add(person)
#session.commit()
perons = session.query(Person).all()
for person in perons:
    print(person)
    print("person %s with id %d"% (person.username, person.id)) 

session.close()
