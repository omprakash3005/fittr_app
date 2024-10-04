from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Diet Plan model
class DietPlan(SQLModel, table=True):
    __tablename__ = "dietplan"
    __table_args__ = {"extend_existing": True}  # Allow redefinition if already exists
    diet_plan_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False)
    dietitian_user_id: int = Field(foreign_key="user.user_id", nullable=False)  # Links to the dietitian
    proteins: float = Field(nullable=False)
    carbs: float = Field(nullable=False)
    fats: float = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    plan_status: str = Field(default="active", max_length=20)

# from sqlmodel import SQLModel, Field
# from typing import Optional
# from datetime import datetime

# # Diet Plan model
# class DietPlan(SQLModel, table=True):
#     __tablename__ = "dietplan"
#     __table_args__ = {"extend_existing": True}  # Allow redefinition if already exists
#     diet_plan_id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="user.user_id", nullable=False)
#     dietitian_user_id: int = Field(foreign_key="user.user_id", nullable=False)  # Links to the dietitian
#     proteins: float = Field(nullable=False)
#     carbs: float = Field(nullable=False)
#     fats: float = Field(nullable=False)
#     created_at: datetime = Field(default_factory=datetime.now)
#     updated_at: Optional[datetime] = Field(default=None)
#     plan_status: str = Field(default="active", max_length=20)
