from fastapi import APIRouter, Depends, status

from src.account.models import Account
from src.movement.models import Movement,MovementCreate
from src.database import get_session
from sqlmodel import select, Session

router = APIRouter(prefix="/movement", tags=["Movement"])

@router.get("/")
def read_movements(session: Session = Depends(get_session)):
    select_statement = select(Movement)
    movements = session.exec(select_statement).all()
    return {"data": movements, "status_code": status.HTTP_200_OK}


@router.post("/", response_model=Movement)
def create_movement(movement: MovementCreate = Depends(), session: Session = Depends(get_session)):
    db_movement = Movement.model_validate(movement)
    account = session.get(Account,movement.account_id)
    if not account:
        return {"data": {}, "status_code": status.HTTP_404_NOT_FOUND}
    account.balance += movement.amount
    session.add(db_movement)
    session.add(account)
    session.commit()
    session.refresh(db_movement)
    return {"data": db_movement, "status_code": status.HTTP_200_OK}