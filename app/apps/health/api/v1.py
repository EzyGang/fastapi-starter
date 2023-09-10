from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from app.apps.health.dtos import PingResponse
from app.core.logging_config import get_logger

logger = get_logger(__name__)
router = APIRouter(
    prefix='/health',
    tags=['health'],
    default_response_class=ORJSONResponse,
)


@router.get('/ping', response_model=PingResponse, status_code=status.HTTP_200_OK)
async def ping() -> PingResponse:
    logger.info(f'Ping request')
    return PingResponse()
