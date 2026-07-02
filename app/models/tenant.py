from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, insert_default=True)

    flags = relationship("FeatureFlag", back_populates="tenant", cascade="all, delete-orphan")