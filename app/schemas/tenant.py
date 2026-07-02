from pydantic import BaseModel

class TenantBase(BaseModel):
    id: str
    name: str

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    is_active: bool

    class Config:
        from_attributes = True
