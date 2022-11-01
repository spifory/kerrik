import asyncio
from logging import basicConfig, INFO
from kerrik.bot import Kerrik


async def start() -> None:
    bot = Kerrik()
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )
    await bot.run()

if __name__ == "__main__":
    asyncio.run(start())
