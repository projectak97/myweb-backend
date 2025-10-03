from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
import json
from app.db import database

router = APIRouter()

class SecurityPatchResponse(BaseModel):
    id: int
    version: str
    title: str
    description: str
    severity: str
    release_date: datetime
    changelog: List[str]
    download_url: str | None
    is_published: bool

    @classmethod
    def from_dict(cls, patch: dict):
        return cls(
            id=patch["id"],
            version=patch["version"],
            title=patch["title"],
            description=patch["description"],
            severity=patch["severity"],
            release_date=patch["release_date"],
            changelog=json.loads(patch["changelog"]) if isinstance(patch["changelog"], str) else patch["changelog"],
            download_url=patch.get("download_url"),
            is_published=patch["is_published"]
        )

@router.get("/", response_model=List[SecurityPatchResponse])
async def get_security_patches(published_only: bool = True):
    patches = database.patches_db.copy()
    
    if published_only:
        patches = [p for p in patches if p["is_published"]]
    
    # Sort by release_date descending
    patches.sort(key=lambda x: x["release_date"], reverse=True)
    
    return [SecurityPatchResponse.from_dict(patch) for patch in patches]

@router.get("/{patch_id}", response_model=SecurityPatchResponse)
async def get_security_patch(patch_id: int):
    patch = next((p for p in database.patches_db if p["id"] == patch_id), None)
    
    if not patch:
        raise HTTPException(status_code=404, detail="Security patch not found")
    
    return SecurityPatchResponse.from_dict(patch)
