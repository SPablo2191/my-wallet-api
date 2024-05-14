from fastapi import APIRouter,Depends

router = APIRouter(prefix='/account', tags=['account'])

@router.get('/')
def get_accounts():
    return {"accounts": []}