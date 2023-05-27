from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Email(Base):
    __tablename__="Email"

    id= Column(Integer, primary_key=True, autoincrement=True)
    mail= Column(String[256])
    user_id = Column(Integer, ForeignKey('User.id'),nullable=False)#, ondelete='CASCADE'
    
class PhoneNumber(Base):
    __tablename__="PhoneNumber"

    id= Column(Integer, primary_key=True, autoincrement=True)
    number= Column(String[30])
    user_id = Column(Integer, ForeignKey('User.id'),nullable=False)

class User(Base):
    __tablename__ = "User"

    id= Column(Integer, primary_key=True, autoincrement=True)
    lastName=Column(String[256])
    firstName=Column(String[256])
    emails= relationship("Email", backref="usr_mail", cascade="all, delete")
    phoneNumbers= relationship("PhoneNumber", backref="usr_number", cascade="all, delete")



