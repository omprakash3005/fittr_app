from db import get_session
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.dietitian.models import DietPlan
from app.dietitian.service import (
    create_diet_plan,
    update_diet_plan,
    delete_diet_plan,
    get_diet_plan,
    fetch_all_diet_plans  # Updated function name to avoid recursion
)

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

@router.delete("/dietplans/{diet_plan_id}", response_model=dict)
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

@router.get("/dietplans/", response_model=list[DietPlan])
async def get_all_diet_plans_route(db: Session = Depends(get_session)):
    return await fetch_all_diet_plans(db)  # Updated to call the correct function


# from db import get_session
# from fastapi import APIRouter, Depends, HTTPException
# from sqlmodel import Session
# from app.dietitian.models import DietPlan
# from app.dietitian.service import (
#     create_diet_plan,
#     update_diet_plan,
#     delete_diet_plan,
#     get_diet_plan,
# )

# router = APIRouter()

# @router.post("/dietplans/", response_model=DietPlan)
# async def create_new_diet_plan(diet_plan: DietPlan, db: Session = Depends(get_session)):
#     return await create_diet_plan(diet_plan, db)

# @router.put("/dietplans/{diet_plan_id}", response_model=DietPlan)
# async def update_existing_diet_plan(diet_plan_id: int, diet_plan: DietPlan, db: Session = Depends(get_session)):
#     existing_plan = await get_diet_plan(diet_plan_id, db)
#     if existing_plan is None:
#         raise HTTPException(status_code=404, detail="Diet plan not found")
#     updated_plan = await update_diet_plan(diet_plan_id, diet_plan, db)
#     return updated_plan

# @router.delete("/dietplans/{diet_plan_id}", response_model=dict)
# async def delete_diet_plan(diet_plan_id: int, db: Session = Depends(get_session)):
#     existing_plan = await get_diet_plan(diet_plan_id, db)
#     if existing_plan is None:
#         raise HTTPException(status_code=404, detail="Diet plan not found")
#     await delete_diet_plan(diet_plan_id, db)
#     return {"message": "Diet plan deleted"}

# @router.get("/dietplans/{diet_plan_id}", response_model=DietPlan)
# async def get_diet_plan_by_id(diet_plan_id: int, db: Session = Depends(get_session)):
#     diet_plan = await get_diet_plan(diet_plan_id, db)
#     if diet_plan is None:
#         raise HTTPException(status_code=404, detail="Diet plan not found")
#     return diet_plan

# @router.get("/dietplans/", response_model=list[DietPlan])
# async def get_all_diet_plans(db: Session = Depends(get_session)):
#     return await get_all_diet_plans(db)
