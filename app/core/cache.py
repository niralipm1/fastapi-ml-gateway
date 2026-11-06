import hashlib
from typing import Optional

class SemanticMemoryCache:
    def __init__(self):
        self._store: dict[str, str] = {}

    def compute_prompt_hash(self, model: str, prompt: str, temperature: float) -> str:
        payload = f"{model}:{temperature}:{prompt.strip()}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    async def get(self, key: str) -> Optional[str]:
        return self._store.get(key)

    async def set(self, key: str, value: str, ttl_seconds: int = 3600) -> None:
        self._store[key] = value

    async def clear(self) -> None:
        self._store.clear()

cache = SemanticMemoryCache()
