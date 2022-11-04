import asyncio
from logging import basicConfig, INFO, getLogger
from kerrik.bot import Kerrik
from os import listdir
from importlib import import_module


async def start() -> None:
    client = Kerrik()
    log = getLogger(__name__)
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )
    for e in listdir("kerrik/exts"):
        if e.endswith(".py"):
            try:
                import_module(f"kerrik.exts.{e[:-3]}").setup(client)
                log.info(f"{e} has loaded")
            except Exception as e:
                log.error("Error while loading extensions: %s", e)
                log.info("Aborting connection")
                exit(1)
    await client.start()

if __name__ == "__main__":
    asyncio.run(start())
