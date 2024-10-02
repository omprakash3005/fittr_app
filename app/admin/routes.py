from fastapi import APIRouter, Depends, HTTPException
from app.admin.service import create_dietitian, update_dietitian, delete_dietitian, get_dietitian
from app.admin.models import Dietitian

router = APIRouter()

@router.post("/dietitians/")
def create_new_dietitian(dietitian: Dietitian):
    return create_dietitian(dietitian)

@router.put("/dietitians/{dietitian_id}", response_model=Dietitian)
def update_existing_dietitian(dietitian_id: int, dietitian: Dietitian):
    return update_dietitian(dietitian_id, dietitian)

@router.delete("/dietitians/{dietitian_id}")
def delete_dietitian_by_id(dietitian_id: int):
    delete_dietitian(dietitian_id)
    return {"message": "Dietitian deleted"}

@router.get("/dietitians/{dietitian_id}", response_model=Dietitian)
def get_dietitian_by_id(dietitian_id: int):
    return get_dietitian(dietitian_id)
