from ..database.database import Base
from sqlalchemy import Integer,String,Column,TIMESTAMP

class User(Base):
    __tablename__ = "Users"
    
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False )
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    role = Column(String,nullable=False,default="user")
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default='now()')