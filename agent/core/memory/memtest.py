import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from core.memory import MemoryManager

async def test():
    m = MemoryManager(redis_url="redis://:123456@localhost:6379",embedding_api_key="sk-87fbe26faae54fabb99a97e8bdbbe3d9")
    await m.initialize()
    print(f"Short-term: {m.short_term.available}")
    print(f"Long-term: {m.long_term.available}")
    await m.close()

asyncio.run(test())