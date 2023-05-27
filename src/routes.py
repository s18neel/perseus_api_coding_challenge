from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import Request, Response, RequestUser, RequestUserNewEmailOrPhone, RequestUpdateUserEmailOrPhone
import pdb

import crud as crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_user(request: RequestUser, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter)
    return Response(status="Ok", code="200", message="User created successfully", result=None).dict(exclude_none=True)

@router.get("/{id}")
async def get_user_by_id(id:int, db:Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, user_id=id)
    return Response(status="Ok", code="200", message="Success fetch user by id", result=_user)

@router.get("/getuserbyname")
async def get_user_by_name(request: RequestUser, db:Session = Depends(get_db)):
    _user = crud.get_user_by_name(db, user = request.parameter)
    return Response(status="Ok", code="200", message="Success fetch user by name", result=_user)

@router.post("/addphonebyuserid")
async def add_user_phone_by_id(request: RequestUserNewEmailOrPhone, db: Session = Depends(get_db)):
    pdb.set_trace()
    _phonedata = crud.add_extra_phone_by_id(db, details= request.parameter)
    return Response(status="Ok", code="200", message="User phone data added successfully", result=_phonedata)

@router.post("/addemailbyuserid")
async def add_user_email_by_id(request: RequestUserNewEmailOrPhone, db: Session = Depends(get_db)):
    pdb.set_trace()
    _emaildata = crud.add_extra_email_by_id(db, details= request.parameter)
    return Response(status="Ok", code="200", message="User email data added successfully", result=_emaildata)

@router.put("/updatephonebyuserid")
async def update_user_phone_by_id(request: RequestUpdateUserEmailOrPhone, db: Session = Depends(get_db)):
    pdb.set_trace()
    _phonedata = crud.update_phone_by_id(db, details = request.parameter)
    return Response(status="Ok", code="200", message="User phone data updated successfully", result=_phonedata)

@router.put("/updateemailbyuserid")
async def update_user_email_by_id(request: RequestUpdateUserEmailOrPhone, db: Session = Depends(get_db)):
    pdb.set_trace()
    _emaildata = crud.update_email_by_id(db, details = request.parameter)
    return Response(status="Ok", code="200", message="User email data updated successfully", result=_emaildata)

@router.delete('/deleteuser')
async def delete_user(request:RequestUser, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id=request.parameter.id)  #type:ignore
    return Response(status="Ok", code="200", message="User Deleted Successfully").dict(exclude_none=True)  #type:ignore




# @router.post("/create")
# async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
#     crud.create_book(db, book=request.parameter)
#     return Response(status="Ok", code="200", message="Book created successfully", result=None).dict(exclude_none=True)

# @router.get("/")
# async def get_books(skip: int = 0, limit:int = 0, db: Session = Depends(get_db)):
#     _books = crud.get_book(db, skip, limit)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=_books)

# @router.get("/{id}")
# async def get_books_by_id(id:int, db: Session = Depends(get_db)):
#     _books = crud.get_book_by_id(db, book_id=id)
#     return Response(status="Ok", code="200", message="Success fetch all data", result=_books)

# @router.patch("/update")
# async def update_books(request: RequestBook, db: Session = Depends(get_db)):
#     _books = crud.update_book(db, book_id=request.parameter.id, title= request.parameter.title, description=request.parameter.description) #type:ignore
#     return Response(status="Ok", code="200", message="Success update data", result=_books)

# @router.delete('/delete')
# async def delete_books(request:RequestBook, db: Session = Depends(get_db)):
#     crud.remove_book(db, book_id=request.parameter.id)  #type:ignore
#     return Response(status="Ok", code="200", message="Book Deleted Successfully").dict(exclude_none=True)  #type:ignore