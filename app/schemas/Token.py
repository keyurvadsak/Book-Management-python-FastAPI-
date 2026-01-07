from pydantic import BaseModel
from typing import Optional


    

class Token(BaseModel):
    access_token : str
    token_type : str
    
class Token_Data(BaseModel):
    id : Optional[int] = None
    role : Optional[str] = None