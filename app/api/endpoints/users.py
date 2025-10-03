from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List
from app.db.database import get_session
from app.models.models import User, UserRole
from app.api.endpoints.auth import get_current_user
from pydantic import BaseModel

router = APIRouter()

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    role: UserRole
    company: str | None
    is_active: bool

@router.get("/", response_model=List[UserResponse])
async def get_users(
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    # Only admins can list users
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    result = await session.execute(select(User))
    users = result.scalars().all()
    
    return users
