from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class FeatureFlagBase(BaseModel):
    key: str
    is_enabled: bool = False
    rollout_percentage: int = Field(defulat=100, ge=0, le=100)
    targeting_rules: Optional[Dict[str, Any]] = None

class FeatureFlagCreate(FeatureFlagBase):
    pass

class FeatureFlagResponse(FeatureFlagBase):
    id: int
    tenant_id: str

    class Config:
        from_attributes = True

class EvaluationRequest(BaseModel):
    user_id: str
    context: Optional[Dict[str, Any]] = Field(default_factory=dict)
