from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Dietitian model (only managed by admin)
class Dietitian(SQLModel, table=True):
    dietitian_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False)
    qualification: str = Field(max_length=255, nullable=False)
    experience_years: int = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)
