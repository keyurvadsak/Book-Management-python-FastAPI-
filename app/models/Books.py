from ..database.database import Base
from sqlalchemy import Integer,String,Column,ForeignKey
from sqlalchemy.orm import relationship




class Books(Base):
    
    __tablename__ = "Books"
    
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False )
    Book_name = Column(String,nullable=False)
    Author_name = Column(String,nullable=False)
    Book_price = Column(Integer, nullable=False)
    owner_id = Column(Integer,ForeignKey("Users.id",ondelete="CASCADE"),nullable=False)
    # created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default='now()')
    owner = relationship("User")