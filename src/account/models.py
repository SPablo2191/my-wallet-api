from decimal import Decimal
from typing import Optional
from sqlmodel import Field,SQLModel
import uuid

class Account(SQLModel,table=True):
    id : Optional[uuid.uuid4] = Field(default=uuid.uuid4(),primary_key=True)
    name : str
    balance : Decimal = Field(default=0, max_digits=5, decimal_places=3)