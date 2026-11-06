from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.schemas import InferenceRequest, InferenceResponse
from app.services.inference_service import inference_service

router = APIRouter()

@router.post("/predict", response_model=InferenceResponse)
async def generate_prediction(request: InferenceRequest):
    return await inference_service.process_inference(request)

@router.post("/predict/stream")
async def stream_prediction(request: InferenceRequest):
    return StreamingResponse(
        inference_service.stream_tokens(request),
        media_type="text/event-stream"
    )
