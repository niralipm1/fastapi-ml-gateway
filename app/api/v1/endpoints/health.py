from fastapi import APIRouter
from app.models.schemas import HealthResponse
from app.core.config import settings

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="HEALTHY",
        version=settings.VERSION,
        cache_ready=True,
        active_workers=8
    )
