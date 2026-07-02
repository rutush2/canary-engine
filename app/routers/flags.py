from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.flag import FeatureFlag
from app.schemas.flag import FeatureFlagCreate, FeatureFlagResponse, EvaluationRequest
from app.services.evaluator import EngineEvaluator

router = APIRouter(prefix="/api/tenants/{tenant_id}/flags", tags=["Feature Flags"])


@router.post("/", response_model=FeatureFlagResponse, status_code=status.HTTP_201_CREATED)
async def create_flag(tenant_id: str, flag_data: FeatureFlagCreate, db: AsyncSession = Depends(get_db)):
    query = select(FeatureFlag).where(FeatureFlag.tenant_id == tenant_id, FeatureFlag.key == flag_data.key)
    if (await db.execute(query)).scalars().first():
        raise HTTPException(status_code=400, detail="Flag key already exists for this tenant.")

    new_flag = FeatureFlag(tenant_id=tenant_id, **flag_data.model_dump())
    db.add(new_flag)

    # Force SQLAlchemy to write to the database and generate the auto-increment ID
    await db.flush()
    await db.refresh(new_flag)

    return new_flag

@router.get("/", response_model=list[FeatureFlagResponse])
async def list_flags(tenant_id: str, db: AsyncSession = Depends(get_db)):
    query = select(FeatureFlag).where(FeatureFlag.tenant_id == tenant_id)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/{flag_key}/evaluate")
async def evaluate_flag(tenant_id: str, flag_key: str, request: EvaluationRequest, db: AsyncSession = Depends(get_db)):
    query = select(FeatureFlag).where(FeatureFlag.tenant_id == tenant_id, FeatureFlag.key == flag_key)
    flag = (await db.execute(query)).scalars().first()

    if not flag:
        raise HTTPException(status_code=404, detail="Feature flag profile not found.")

    is_variant_active = EngineEvaluator.evaluate(flag, request.user_id, request.context)
    return {"flag_key": flag_key, "user_id": request.user_id, "enabled": is_variant_active}