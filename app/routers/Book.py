from fastapi import APIRouter,Depends, Response,status,HTTPException,Request
from ..models.models import get_db
from ..schemas.Book import BookCreate,BookOut,BookList,UpdateBook
from sqlalchemy.orm import Session
from ..models.Books import Books
from ..routers.Oauth2 import get_current_user
from ..limiter.limiter import limiter


router = APIRouter(
    prefix= "/Books",
    tags=['Books']
)


@router.post("/",response_model=BookOut,status_code=status.HTTP_201_CREATED)
@limiter.limit("2/minute")
def create_book(request:Request,book:BookCreate,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    new_book = Books(**book.dict(),owner_id= current_user.id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/",response_model= list[BookList])
@limiter.limit("10/minute")
def get_user_books(request:Request,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    book = db.query(Books).all()
    return book

@router.get("/own_Books",response_model= list[BookList])
@limiter.limit("5/minute")
def get_user_books(request:Request,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    book = db.query(Books).filter(Books.owner_id == current_user.id).all()
    return book

@router.delete("/{id}")
@limiter.limit("2/minute")
def delete_books(request:Request,id:int,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    delete_books = db.query(Books).filter(Books.id == id)
    if delete_books.first() == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail=f"post with id {id} is not found.")
    if delete_books.first().owner_id != current_user.id and current_user.role == "admin":
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail="Access are denied.")
    delete_books.delete(synchronize_session= False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model= BookOut,status_code=status.HTTP_202_ACCEPTED)
@limiter.limit("2/minute")
def update_book(request:Request,id:int,book:UpdateBook,db:Session =Depends(get_db),current_user = Depends(get_current_user)):
    update_book_query = db.query(Books).filter(Books.id == id)
    
    if update_book_query.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"post with id {id} is not found.")
    print(update_book_query.first().owner_id,"   ",current_user.id,"   ",current_user.role)
    if update_book_query.first().owner_id != current_user.id or current_user.role == "admin":
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail="Access are denied.")
        
    update_book_query.update(book.dict(),synchronize_session= False)
    db.commit()
    return update_book_query.first()