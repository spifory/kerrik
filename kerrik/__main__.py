import asyncio
from logging import basicConfig, INFO, getLogger
from kerrik.bot import Kerrik
from pathlib import Path


async def start() -> None:
    client = Kerrik()
    log = getLogger(__name__)
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )
    try:
        for c in Path("kerrik/exts").glob("**/*.py"):
            client.load(f"kerrik.exts.{c.stem}")
            log.info(f"Loaded extension {c.stem}")
    except Exception as e:
        log.error(f"Error while loading extension \"{c}\": {e}")  # type: ignore
        log.info("Aborting connection")
        exit(1)
    await client.start()

if __name__ == "__main__":
    asyncio.run(start())
