import asyncio
import time
import uuid
from typing import AsyncGenerator
from app.core.cache import cache
from app.models.schemas import InferenceRequest, InferenceResponse

class InferenceService:
    async def process_inference(self, req: InferenceRequest) -> InferenceResponse:
        start_time = time.perf_counter()
        cache_key = cache.compute_prompt_hash(req.model, req.prompt, req.temperature)

        # Check semantic cache
        cached_result = await cache.get(cache_key)
        if cached_result:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return InferenceResponse(
                id=f"inf_{uuid.uuid4().hex[:8]}",
                model=req.model,
                output_text=cached_result,
                cached=True,
                latency_ms=round(elapsed_ms, 2),
                total_tokens=len(cached_result.split()) * 2
            )

        # Simulates asynchronous tensor inference
        await asyncio.sleep(0.08) # 80ms simulation
        simulated_output = (
            f"Synthesized response for query regarding: '{req.prompt[:60]}...'\n"
            f"Generated via {req.model} with high fidelity."
        )

        await cache.set(cache_key, simulated_output)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        return InferenceResponse(
            id=f"inf_{uuid.uuid4().hex[:8]}",
            model=req.model,
            output_text=simulated_output,
            cached=False,
            latency_ms=round(elapsed_ms, 2),
            total_tokens=len(simulated_output.split()) * 2
        )

    async def stream_tokens(self, req: InferenceRequest) -> AsyncGenerator[str, None]:
        tokens = [
            "Processing", " request", " through", " distributed",
            " tensor", " engine.", " Generating", " high", "-assurance",
            " output", " tokens."
        ]
        for token in tokens:
            await asyncio.sleep(0.02)
            yield f"data: {token}\n\n"
        yield "data: [DONE]\n\n"

inference_service = InferenceService()
