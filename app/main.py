from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .db.db import Base, engine, sessionLocal, get_db, User
from app.schema.schema import userCreate, userOutput
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post('/users', status_code = status.HTTP_201_CREATED, response_model=userCreate)
async def create_user(user:userCreate, db:Session = Depends(get_db)):
    request_email = db.query(User).filter(User.email == user.email).first()
    if request_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail = f"Email id {user.email} already exists")
    else:
        temp_user = user.dict().copy()
        new_user = User(**temp_user)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

    return new_user

@app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=userOutput)
async def get_user(id: int, db : Session = Depends(get_db)):
    user_information = db.query(User).filter(User.uid == id).first()
    return user_information

@app.delete('/users/{id}',status_code=status.HTTP_200_OK)
def delete(id: int, db : Session = Depends(get_db))
