from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from typing import Optional, Dict, Any

class FeatureFlag(Base):
    __tablename__ = "feature_Flags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("tenants.id", ondelete="CASCADE"), index=True)
    key: Mapped[str] = mapped_column(index=True, nullable=False)
    is_enabled: Mapped[bool] = mapped_column(default=100)
    rollout_percentage: Mapped[int] = mapped_column(default=100)
    targeting_rules: Mapped[Optional[Dict[str, Any]]] = mapped_column(JSON, nullable=True)

    tenant = relationship("Tenant", back_populates="flags")