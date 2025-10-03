from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"
    PARTNER = "partner"
    PROSPECT = "prospect"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    full_name: str
    role: UserRole = Field(default=UserRole.PROSPECT)
    company: Optional[str] = None
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    contacts: List["Contact"] = Relationship(back_populates="user")

class ServiceCategory(str, Enum):
    CAMERA = "camera"
    FLIGHT_CONTROL = "flight_control"
    SECURITY = "security"
    OPTIMIZATION = "optimization"
    EMERGENCY = "emergency"

class Service(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    slug: str = Field(unique=True, index=True)
    description: str
    category: ServiceCategory
    features: str  # JSON string
    benefits: str  # JSON string
    icon: Optional[str] = None
    image_url: Optional[str] = None
    is_featured: bool = Field(default=False)
    order_index: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ContactStatus(str, Enum):
    NEW = "new"
    CONTACTED = "contacted"
    QUALIFIED = "qualified"
    CONVERTED = "converted"
    CLOSED = "closed"

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    full_name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    message: str
    service_interest: Optional[str] = None
    status: ContactStatus = Field(default=ContactStatus.NEW)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    user: Optional[User] = Relationship(back_populates="contacts")

class DemoRequest(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str
    company: str
    phone: Optional[str] = None
    service_type: ServiceCategory
    preferred_date: Optional[datetime] = None
    message: Optional[str] = None
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SecurityPatch(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: str
    title: str
    description: str
    severity: str  # low, medium, high, critical
    release_date: datetime
    changelog: str  # JSON string
    download_url: Optional[str] = None
    is_published: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
