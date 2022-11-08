import asyncio
from logging import basicConfig, INFO, getLogger
from kerrik.bot import Kerrik
from pathlib import Path
from disnake.ext.commands import ExtensionError


async def start() -> None:
    bot = Kerrik()
    log = getLogger(__name__)
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )
    try:
        for c in Path("kerrik/exts").glob("**/*.py"):
            bot.load_extension(f"kerrik.exts.{c.stem}")
    except ExtensionError as e:
        log.error(f"Error while loading extension \"{e.name}\": {e}")
        log.info("Aborting connection")
        exit(1)
    await bot.start(bot.config["TOKEN"])

if __name__ == "__main__":
    asyncio.run(start())
