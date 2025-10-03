from fastapi import APIRouter
from typing import List
from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.db import database

router = APIRouter()

class DemoRequestCreate(BaseModel):
    full_name: str
    email: EmailStr
    company: str
    phone: str | None = None
    service_type: str
    preferred_date: datetime | None = None
    message: str | None = None

class DemoRequestResponse(BaseModel):
    id: int
    full_name: str
    email: str
    company: str
    phone: str | None
    service_type: str
    preferred_date: datetime | None
    message: str | None
    status: str
    created_at: datetime

@router.post("/", response_model=DemoRequestResponse)
async def create_demo_request(demo_data: DemoRequestCreate):
    demo = {
        "id": database.get_next_id("demo"),
        **demo_data.model_dump(),
        "status": "pending",
        "created_at": datetime.utcnow()
    }
    database.demos_db.append(demo)
    
    return DemoRequestResponse(**demo)

@router.get("/", response_model=List[DemoRequestResponse])
async def get_demo_requests(status: str | None = None):
    demos = database.demos_db.copy()
    
    if status:
        demos = [d for d in demos if d["status"] == status]
    
    # Sort by created_at descending
    demos.sort(key=lambda x: x["created_at"], reverse=True)
    
    return [DemoRequestResponse(**demo) for demo in demos]
