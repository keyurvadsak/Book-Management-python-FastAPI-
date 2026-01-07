from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'],deprecated = "auto")

def hash_password(password):
    h_password = password_context.hash(password)
    
    return h_password

def verify_hashpassword(plain_password,hashed_password):
    
    return password_context.verify(plain_password,hashed_password)