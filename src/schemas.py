from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

class EmailSchema(BaseModel):
    mail = str

class PhoneNumberSchema(BaseModel):
    number = str

class UserSchema(BaseModel):
    id: Optional[int] = None
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    emails: list[EmailSchema]
    phoneNumbers: list[PhoneNumberSchema]

    class config:
        orm_mode = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class AddUserEmailOrPhone(BaseModel):
    user_id: int
    phonenum: Optional[str] = None
    email: Optional[str] = None


class RequestUserNewEmailOrPhone(BaseModel):
    parameter: AddUserEmailOrPhone = Field(...)


class UpdateUserEmailOrPhone(BaseModel):
    user_id: int
    oldphonenum: Optional[str] = None
    newphonenum: Optional[str] = None
    oldemail: Optional[str] = None
    newemail: Optional[str] = None

class RequestUpdateUserEmailOrPhone(BaseModel):
    parameter: UpdateUserEmailOrPhone = Field(...)




class Request(GenericModel, Generic[T]):
    parameters: Optional[T] = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] 
