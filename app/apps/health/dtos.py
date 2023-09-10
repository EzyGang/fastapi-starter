from app.core.pydantic_base import BaseModel


class PingResponse(BaseModel):
    ping: str = 'pong'
