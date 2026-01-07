from fastapi import APIRouter,Depends,status,HTTPException,Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models.models import get_db
from ..models.User import User
from ..utils.utils import verify_hashpassword
from .Oauth2 import create_access_token
from ..schemas.User import UserCreate
from ..utils.utils import hash_password
from logger import setup_logger
from ..limiter.limiter import limiter

logger = setup_logger()

router = APIRouter(
    prefix="/auth",
    tags=['Auth']
)


@router.post('/login')
@limiter.limit("5/minute")
def login(request:Request,user_login:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_login.username).first()
    logger.info(f"Login attempt for user: {user_login.username}")
    if user == None:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail = "Invaild Email.")
    
    if verify_hashpassword(user_login.password,user.password) == False:
        logger
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail = "Invaild Password.")
    
    
    access_token = create_access_token(data = {"user_id":user.id,"role":user.role})
    return {"access_token":access_token,"token_type":"Bearer"}
    # logger.info(f"User {user.email} logged in successfully.")
    
    
@router.post("/register")
def register_User(users : UserCreate, db:Session = Depends(get_db)):

    new_user = User(**users.dict())
    h_password = hash_password(new_user.password)
    new_user.password = h_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user




