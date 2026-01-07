from pydantic import BaseModel
from .User import UserOutforBook


class Book(BaseModel):
    Book_name : str
    Author_name : str
    Book_price : int
class BookCreate(Book):
    pass

class UpdateBook(Book):
    pass

class BookOut(BaseModel):
    id : int
    Book_name : str
    Author_name : str
    Book_price : int
    owner_id : int
    owner: UserOutforBook

    model_config={
        "from_attributes": True
    }
    
class BookList(BaseModel):
    Book_name : str
    Author_name : str
    Book_price : int
    
