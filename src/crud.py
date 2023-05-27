from sqlalchemy.orm import Session
from model import User,Email,PhoneNumber
from schemas import UserSchema
import pdb


# def get_book(db:Session, skip:int=0, limit:int=100):
#     return db.query(Book).offset(skip).limit(limit).all()

# def get_book_by_id(db:Session, book_id:int):
#     return db.query(Book).filter(Book.id == book_id).first()

# def get_user(db:Session, skip:int=0, limit:int=100):
#     return db.query(User).offset(skip).limit(limit).all()

def get_user_by_name(db:Session, user:UserSchema):
    firstname, lastname = user.firstName, user.lastName
    return db.query(User).filter(User.firstName == firstname, User.lastName == lastname).first()

def get_user_by_id(db:Session, user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db:Session, user:UserSchema):
    _user = User(firstName =user.firstName,lastName=user.lastName)
    db.add(_user)
    db.commit()
    db.refresh(_user)

    user_obj = db.query(User).order_by(User.id.desc()).first()

    add_phone_numbers(db, user.phoneNumbers, user_obj)
    add_emails(db, user.phoneNumbers, user_obj)
    
    return _user

def add_phone_numbers(db, phone_numbers, user_obj):
    _phonenumbers = [PhoneNumber(number=item['number'], usr_number = user_obj) for item in phone_numbers]
    if len(_phonenumbers)>=1:
        db.add_all(_phonenumbers)
        db.commit()

def add_emails(db, emails, user_obj):
    _emails = [Email(mail=item['mail'], usr_mail = user_obj) for item in emails]
    if len(_emails)>=1:
        db.add_all(_emails)
        db.commit()

def add_extra_phone_by_id(db, details):
    user_id , phone_number = details.user_id, details.phonenum
    _user = get_user_by_id(db,user_id=user_id)
    if _user is not None:
        _user_id = _user.id         #type:ignore
        print(f'User Id:{_user_id}')
        _phonedata = PhoneNumber(number=phone_number, user_id= _user_id)
        db.add(_phonedata)
        db.commit()
        db.refresh(_phonedata)
        return _phonedata
    else:
        return "User Not Found"
    
def add_extra_email_by_id(db, details):
    pdb.set_trace()
    user_id , email = details.user_id, details.email
    _user = get_user_by_id(db,user_id=user_id)
    if _user is not None:
        _user_id = _user.id         #type:ignore
        print(f'User Id:{_user_id}')
        _emaildata = Email(mail=email, user_id= _user_id)
        db.add(_emaildata)
        db.commit()
        db.refresh(_emaildata)
        return _emaildata
    else:
        return "User Not Found"
    
def update_email_by_id(db, details):
    user_id, oldemail, newemail = details.user_id, details.oldemail, details.newemail
    _user = get_user_by_id(db,user_id=user_id)
    if _user is not None:
        _user_id = _user.id         #type:ignore
        print(f'User Id:{_user_id}')
        _emaildata = db.query(Email).filter(Email.user_id == _user_id, Email.mail == oldemail).first()
        if _emaildata is not None:
            _emaildata.mail = newemail
            db.add(_emaildata)
            db.commit()
            db.refresh(_emaildata)
            return _emaildata
        else:
            return "Email for user doesn't exist"
    else:
        return "User Not Found"  

def update_phone_by_id(db, details):
    user_id, oldphone, newphone = details.user_id, details.oldphonenum, details.newphonenum
    _user = get_user_by_id(db,user_id=user_id)
    if _user is not None:
        _user_id = _user.id         #type:ignore
        print(f'User Id:{_user_id}')
        _phonedata = db.query(PhoneNumber).filter(PhoneNumber.user_id == _user_id, PhoneNumber.number == oldphone).first()
        if _phonedata is not None:
            _phonedata.number = newphone
            db.add(_phonedata)
            db.commit()
            db.refresh(_phonedata)
            return _phonedata
        else:
            return "Phone Number for user doesn't exist"
    else:
        return "User Not Found"

def delete_user(db:Session, user_id:int):
    _user = get_user_by_id(db,user_id)
    db.delete(_user)
    db.commit()

# def update_book(db:Session, book_id:int, title:str, description:str):
#     _book = get_book_by_id(db=db, book_id=book_id)
#     _book.title = title #type:ignore
#     _book.description = description #type:ignore
#     db.commit()
#     db.refresh(_book)
#     return _book
