from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate, TenantResponse

router = APIRouter(prefix="/api/tenants", tags=["Tenants"])


@router.post("/", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
async def create_tenant(tenant_data: TenantCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant).where(Tenant.id == tenant_data.id))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Tenant ID already registered.")

    new_tenant = Tenant(id=tenant_data.id, name=tenant_data.name, is_active=True)
    db.add(new_tenant)
    return new_tenant