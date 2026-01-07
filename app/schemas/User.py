from pydantic import BaseModel,EmailStr



class UserCreate(BaseModel):
    name :str
    email:EmailStr
    password : str

class UserOutforBook(BaseModel):
    id : int
    name : str
    email : EmailStr

    model_config={
        "from_attributes": True
    }

class LoginUser(BaseModel):
    username : EmailStr
    password : str
