import os
from types import TracebackType
import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


class MCPClient(MultiServerMCPClient):
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await super().__aexit__(exc_type, exc_val, exc_tb)

        # Give a moment for cleanup on Windows
        if os.name == 'nt':
            await asyncio.sleep(0.1)

