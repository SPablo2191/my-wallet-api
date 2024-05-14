from fastapi import APIRouter, Depends, status

from src.account.models import Account,AccountCreate
from src.database import get_session
from sqlmodel import select, Session

router = APIRouter(prefix="/account", tags=["Account"])


@router.get("/")
def read_accounts(session: Session = Depends(get_session)):
    select_statement = select(Account)
    accounts = session.exec(select_statement).all()
    return {"data": accounts, "status_code": status.HTTP_200_OK}


@router.post("/", response_model=Account)
def create_account(account: AccountCreate = Depends(), session: Session = Depends(get_session)):
    db_account = Account.model_validate(account)
    session.add(db_account)
    session.commit()
    session.refresh(db_account)
    return {"data": db_account, "status_code": status.HTTP_200_OK}

@router.delete("/{account_id}")
def delete_account(account_id : int, session: Session = Depends(get_session)):
    account = session.get(Account,account_id)
    if not account:
        return {"data": {}, "status_code": status.HTTP_404_NOT_FOUND}
    session.delete(account)
    session.commit()
    return {"data": {}, "status_code": status.HTTP_202_ACCEPTED}

