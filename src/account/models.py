from decimal import Decimal
from typing import Optional
from sqlmodel import Field,SQLModel, Relationship

class Account(SQLModel,table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    balance : Decimal = Field(default=0, max_digits=10, decimal_places=3)
    movements: list["Movement"] = Relationship(back_populates="account")


class AccountCreate(SQLModel):
    name : str = Field("", description="Name of Account")
    balance : Decimal = Field(0, description="Balance of Account")