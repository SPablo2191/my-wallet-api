from fastapi import APIRouter, Depends, status

from src.database import get_session
from src.account.models import Account
from sqlmodel import select, Session

router = APIRouter(prefix="/account", tags=["account"])


@router.get("/")
def read_accounts(session: Session = Depends(get_session)):
    select_statement = select(Account)
    accounts = session.exec(select_statement).all()
    return {"data": accounts, "status_code": status.HTTP_200_OK}


@router.post("/", response_model=Account)
def create_account(account: Account, session: Session = Depends(get_session)):
    session.add(account)
    session.commit()
    session.refresh(account)
    return {"data": account, "status_code": status.HTTP_200_OK}
