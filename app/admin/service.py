from fastapi import HTTPException
from app.admin.models import Dietitian
from db import Session

async def create_dietitian(dietitian: Dietitian):
    async with Session() as session:
        session.add(dietitian)
        await session.commit()
        return dietitian

async def update_dietitian(dietitian_id: int, dietitian: Dietitian):
    async with Session() as session:
        db_dietitian = await session.get(Dietitian, dietitian_id)
        if not db_dietitian:
            raise HTTPException(status_code=404, detail="Dietitian not found")
        db_dietitian.update(dietitian.dict())
        await session.commit()
        return db_dietitian

async def delete_dietitian(dietitian_id: int):
    async with Session() as session:
        db_dietitian = await session.get(Dietitian, dietitian_id)
        if db_dietitian:
            await session.delete(db_dietitian)
            await session.commit()

async def get_dietitian(dietitian_id: int):
    async with Session() as session:
        return await session.get(Dietitian, dietitian_id)
