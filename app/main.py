from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import engine, Base, get_db
from app.models.tenant import Tenant
from app.routers import tenants, flags

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="Multi-Tenant Canary Configuration Engine",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(tenants.router)
app.include_router(flags.router)

templates = Jinja2Templates(directory="templates")

@app.get("/dashboard", response_class=HTMLResponse)
async def render_dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant))
    tenants_list = result.scalars().all()
    return templates.TemplateResponse("dashboard.html", {"request": request, "tenants": tenants_list})

@app.get("/health")
async def health_check():
    return {"status": "healthy", "engine": "operational"}