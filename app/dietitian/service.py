from datetime import datetime
from sqlmodel import Session, select
from app.dietitian.models import DietPlan

async def create_diet_plan(diet_plan: DietPlan, db: Session):
    # Ensure created_at is set correctly without timezone info
    diet_plan.created_at = datetime.now()  # or datetime.utcnow() for UTC
    db.add(diet_plan)
    await db.commit()
    await db.refresh(diet_plan)
    return diet_plan

async def update_diet_plan(diet_plan_id: int, diet_plan: DietPlan, db: Session):
    existing_plan = await db.get(DietPlan, diet_plan_id)
    if existing_plan:
        existing_plan.proteins = diet_plan.proteins
        existing_plan.carbs = diet_plan.carbs
        existing_plan.fats = diet_plan.fats
        existing_plan.dietitian_user_id = diet_plan.dietitian_user_id
        existing_plan.updated_at = datetime.now()  # or datetime.utcnow() for UTC
        db.add(existing_plan)
        await db.commit()
        await db.refresh(existing_plan)
        return existing_plan
    return None
async def delete_diet_plan(diet_plan_id: int, db: Session):
    diet_plan = await db.get(DietPlan, diet_plan_id)
    if diet_plan:
        await db.delete(diet_plan)
        await db.commit()

async def get_diet_plan(diet_plan_id: int, db: Session):
    return await db.get(DietPlan, diet_plan_id)

async def get_all_diet_plans(db: Session):
    statement = select(DietPlan)
    result = await db.exec(statement)
    return result.all()
