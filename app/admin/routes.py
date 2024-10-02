from fastapi import APIRouter, Depends, HTTPException
from app.admin.service import create_dietitian, update_dietitian, delete_dietitian, get_dietitian
from app.admin.models import Dietitian
from typing import List

router = APIRouter()

@router.post("/dietitians/", response_model=Dietitian)
async def create_new_dietitian(dietitian: Dietitian):
    return await create_dietitian(dietitian)

@router.put("/dietitians/{dietitian_id}", response_model=Dietitian)
async def update_existing_dietitian(dietitian_id: int, dietitian: Dietitian):
    return await update_dietitian(dietitian_id, dietitian)

@router.delete("/dietitians/{dietitian_id}")
async def delete_dietitian(dietitian_id: int):
    await delete_dietitian(dietitian_id)
    return {"message": "Dietitian deleted"}

@router.get("/dietitians/{dietitian_id}", response_model=Dietitian)
async def get_dietitian_by_id(dietitian_id: int):
    return await get_dietitian(dietitian_id)
