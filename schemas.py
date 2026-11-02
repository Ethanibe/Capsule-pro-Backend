from pydantic import BaseModel

class UserSignup(BaseModel):
    Fullname: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class ProductCreate(BaseModel):
    name: str
    price: int
    category: str
    image: str
    oldPrice: int | None = None
    badge: str | None = None

class ProductUpdate(BaseModel):
    name: str | None = None
    price: int | None = None
    category: str | None = None
    image: str | None = None
    oldPrice: int | None = None
    badge: str | None = None
