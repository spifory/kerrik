import asyncio
from logging import basicConfig, INFO
from kerrik.bot import Kerrik
from os import listdir
from importlib import import_module


async def start() -> None:
    client = Kerrik()
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )
    for e in listdir("kerrik/exts"):
        if e.endswith(".py"):
            import_module(f"kerrik.exts.{e[:3]}").setup()
    await client.start()

if __name__ == "__main__":
    asyncio.run(start())
