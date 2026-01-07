
from jose import JWTError,jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from ..schemas.Token import Token_Data
from fastapi import HTTPException,status,Depends
from ..models.models import get_db
from ..models.User import User
from sqlalchemy.orm import Session
from ..config.config import settings


SECRETE_KEY =settings.secret_key
ALGORITHYM =settings.algorithm
EXPIRE_MINUTES =settings.access_token_expire_minutes

Oauth2_sceheme = OAuth2PasswordBearer(tokenUrl= "auth/login")


def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRETE_KEY,algorithm=ALGORITHYM)
    return encoded_jwt


def verify_access_token(token:str,credentials_exception,db:Session = Depends(get_db)):
    try:
        payload = jwt.decode(token=token,key=SECRETE_KEY,algorithms=[ALGORITHYM])
        user_id:str = payload.get("user_id")
        if user_id == None:
            raise credentials_exception
        token_data = Token_Data(id = user_id,role = payload.get("role"))
        return token_data
    except JWTError:
        raise credentials_exception
    
    
    
def get_current_user(token:str  = Depends(Oauth2_sceheme),db:Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token(token,credentials_exception)
    user = db.query(User).filter(User.id == token.id).first()
    
    return user

# def role_check(roles:list):
#     def checker(user = Depends(get_current_user)):
#         if user.role not in roles:
#             raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail="Access Denied.")
#         return user
#     return checker
    