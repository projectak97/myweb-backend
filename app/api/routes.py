from fastapi import APIRouter
from app.api.endpoints import services, contacts, demos, security_patches

api_router = APIRouter()

api_router.include_router(services.router, prefix="/services", tags=["Services"])
api_router.include_router(contacts.router, prefix="/contacts", tags=["Contacts"])
api_router.include_router(demos.router, prefix="/demos", tags=["Demo Requests"])
api_router.include_router(security_patches.router, prefix="/security-patches", tags=["Security Patches"])
