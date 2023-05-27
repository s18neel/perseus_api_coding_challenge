from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

from dataclasses import dataclass

@dataclass
class Config():
    host: str
    username: str
    password: str
    database: str
    port: int

    @property
    def url(self)-> str:
        return f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'
    

config = Config(
    host= os.getenv("POSTGRES_HOST", "localhost"),
    username= os.getenv("POSTGRES_USERNAME", "postgres"),
    password= os.getenv("POSTGRES_PASSWORD", "postgres"),
    database= os.getenv("POSTGRES_DB", "postgres"),
    port= int(os.getenv("POSTGRES_PORT", 5432))
)

engine = create_engine(url=config.url)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)

Base = declarative_base()