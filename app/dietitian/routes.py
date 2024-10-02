from db import get_session
from fastapi import APIRouter, Depends, HTTPException
from app.dietitian.service import create_diet_plan, update_diet_plan, delete_diet_plan, get_diet_plan
from app.dietitian.models import DietPlan
from sqlmodel import Session

router = APIRouter()

@router.post("/dietplans/", response_model=DietPlan)
async def create_new_diet_plan(diet_plan: DietPlan, db: Session = Depends(get_session)):
    return await create_diet_plan(diet_plan, db)

@router.put("/dietplans/{diet_plan_id}", response_model=DietPlan)
async def update_existing_diet_plan(diet_plan_id: int, diet_plan: DietPlan, db: Session = Depends(get_session)):
    existing_plan = await get_diet_plan(diet_plan_id, db)
    if existing_plan is None:
        raise HTTPException(status_code=404, detail="Diet plan not found")
    updated_plan = await update_diet_plan(diet_plan_id, diet_plan, db)
    return updated_plan

@router.delete("/dietplans/{diet_plan_id}")
async def delete_diet_plan(diet_plan_id: int, db: Session = Depends(get_session)):
    existing_plan = await get_diet_plan(diet_plan_id, db)
    if existing_plan is None:
        raise HTTPException(status_code=404, detail="Diet plan not found")
    await delete_diet_plan(diet_plan_id, db)
    return {"message": "Diet plan deleted"}

@router.get("/dietplans/{diet_plan_id}", response_model=DietPlan)
async def get_diet_plan_by_id(diet_plan_id: int, db: Session = Depends(get_session)):
    diet_plan = await get_diet_plan(diet_plan_id, db)
    if diet_plan is None:
        raise HTTPException(status_code=404, detail="Diet plan not found")
    return diet_plan
