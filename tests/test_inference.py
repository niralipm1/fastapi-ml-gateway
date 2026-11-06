import pytest
from app.services.inference_service import InferenceService
from app.models.schemas import InferenceRequest
from app.core.cache import cache

@pytest.mark.asyncio
async def test_inference_caching_lifecycle():
    await cache.clear()
    service = InferenceService()

    req = InferenceRequest(
        prompt="Explain vector embedding indexes in PostgreSQL",
        model="llama-3-70b-instruct",
        temperature=0.5
    )

    # First call: cache miss
    resp1 = await service.process_inference(req)
    assert resp1.cached is False
    assert "Synthesized response" in resp1.output_text

    # Second call: cache hit
    resp2 = await service.process_inference(req)
    assert resp2.cached is True
    assert resp2.output_text == resp1.output_text
    assert resp2.latency_ms < resp1.latency_ms
