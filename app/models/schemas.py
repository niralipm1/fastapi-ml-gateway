from pydantic import BaseModel, Field
from typing import Optional, List

class InferenceRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=32000, description="User instruction prompt")
    model: str = Field(default="llama-3-70b-instruct", description="Target model identifier")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, ge=1, le=4096)
    stream: bool = Field(default=False, description="Enable Server-Sent Events token streaming")

class InferenceResponse(BaseModel):
    id: str
    model: str
    output_text: str
    cached: bool
    latency_ms: float
    total_tokens: int

class HealthResponse(BaseModel):
    status: str
    version: str
    cache_ready: bool
    active_workers: int
