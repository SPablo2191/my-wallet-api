from decimal import Decimal
from typing import Optional
from sqlmodel import Field,SQLModel,Relationship

from src.account.models import Account

class Movement(SQLModel,table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name : str = Field(index=True)
    description : str = Field()
    amount : Decimal = Field(max_digits=10, decimal_places=3)
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")
    account : Optional[Account] = Relationship(back_populates="movements")

class MovementCreate(SQLModel):
    name : str = Field("", description="Name of Account")
    description : str = Field("", description="Name of Account")
    amount : Decimal = Field(0, description="Balance of Account")
    account_id: Optional[int] = Field(default=None, foreign_key="account.id")