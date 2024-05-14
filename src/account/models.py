from decimal import Decimal
from typing import Optional
from sqlmodel import Field,SQLModel

class Account(SQLModel,table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    balance : Decimal = Field(default=0, max_digits=5, decimal_places=3)