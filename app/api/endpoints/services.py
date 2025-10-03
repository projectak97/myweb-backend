from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
import json
from app.db import database

router = APIRouter()

class ServiceResponse(BaseModel):
    id: int
    title: str
    slug: str
    description: str
    category: str
    features: List[str]
    benefits: List[str]
    icon: str | None
    image_url: str | None
    is_featured: bool

    @classmethod
    def from_dict(cls, service: dict):
        return cls(
            id=service["id"],
            title=service["title"],
            slug=service["slug"],
            description=service["description"],
            category=service["category"],
            features=json.loads(service["features"]) if isinstance(service["features"], str) else service["features"],
            benefits=json.loads(service["benefits"]) if isinstance(service["benefits"], str) else service["benefits"],
            icon=service.get("icon"),
            image_url=service.get("image_url"),
            is_featured=service["is_featured"]
        )

@router.get("/", response_model=List[ServiceResponse])
async def get_services(
    featured_only: bool = False,
    category: str | None = None
):
    services = database.services_db.copy()
    
    if featured_only:
        services = [s for s in services if s["is_featured"]]
    
    if category:
        services = [s for s in services if s["category"] == category]
    
    # Sort by order_index
    services.sort(key=lambda x: x["order_index"])
    
    return [ServiceResponse.from_dict(service) for service in services]

@router.get("/{slug}", response_model=ServiceResponse)
async def get_service(slug: str):
    service = next((s for s in database.services_db if s["slug"] == slug), None)
    
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    return ServiceResponse.from_dict(service)

@router.get("/categories/list")
async def get_categories():
    return {
        "categories": [
            {"value": "camera", "label": "Camera Solutions"},
            {"value": "flight_control", "label": "Flight Control"},
            {"value": "security", "label": "Security"},
            {"value": "optimization", "label": "Optimization"},
            {"value": "emergency", "label": "Emergency Systems"}
        ]
    }
