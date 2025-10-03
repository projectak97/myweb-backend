from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.db import database

router = APIRouter()

class ContactCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    message: str
    service_interest: str | None = None

class ContactResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str | None
    company: str | None
    message: str
    service_interest: str | None
    status: str
    created_at: datetime

@router.post("/", response_model=ContactResponse)
async def create_contact(contact_data: ContactCreate):
    contact = {
        "id": database.get_next_id("contact"),
        **contact_data.model_dump(),
        "status": "new",
        "created_at": datetime.utcnow()
    }
    database.contacts_db.append(contact)
    
    return ContactResponse(**contact)

@router.get("/", response_model=List[ContactResponse])
async def get_contacts(status: str | None = None):
    contacts = database.contacts_db.copy()
    
    if status:
        contacts = [c for c in contacts if c["status"] == status]
    
    # Sort by created_at descending
    contacts.sort(key=lambda x: x["created_at"], reverse=True)
    
    return [ContactResponse(**contact) for contact in contacts]

@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contact(contact_id: int):
    contact = next((c for c in database.contacts_db if c["id"] == contact_id), None)
    
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    return ContactResponse(**contact)
