from fastapi import HTTPException
from app.admin.models import Dietitian
from db import Session, engine

def create_dietitian(dietitian):
    with Session(engine) as session:
        new_dietitian = Dietitian(
            name=dietitian.name,
            email=dietitian.email,
            qualification=dietitian.qualification,
            experience_years=dietitian.experience_years,
            user_id=dietitian.user_id,
        )
        session.add(new_dietitian)
        session.commit()
        session.refresh(new_dietitian)
        return {"message": "Dietitian created successfully", "dietitian": new_dietitian}
def update_dietitian(dietitian_id: int, dietitian: Dietitian):
    with Session(engine) as session:
        db_dietitian = session.get(Dietitian, dietitian_id)
        if not db_dietitian:
            raise HTTPException(status_code=404, detail="Dietitian not found")
        for key, value in dietitian.dict(exclude_unset=True).items():
            setattr(db_dietitian, key, value)
        session.commit()
        return db_dietitian
def delete_dietitian(dietitian_id: int):
    with Session(engine) as session:
        db_dietitian = session.get(Dietitian, dietitian_id)
        if db_dietitian:
            session.delete(db_dietitian)
            session.commit()

def get_dietitian(dietitian_id: int):
    with Session(engine) as session:
        dietitian = session.get(Dietitian, dietitian_id)
        if not dietitian:
            raise HTTPException(status_code=404, detail="Dietitian not found")
        return dietitian