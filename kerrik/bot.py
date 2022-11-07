import datetime
from logging import getLogger
from disnake import Activity, ActivityType, Intents
from disnake.ext.commands import Bot, CommandSyncFlags
import os
from dotenv import load_dotenv

LOG = getLogger(__name__)
load_dotenv()


class Kerrik(Bot):
    def __init__(self):
        self.start_time: datetime.datetime
        self.config = os.environ
        super().__init__(
            ["-", "kerrik"],
            help_command=None,  # type: ignore
            case_insensitive=True,
            intents=Intents(
                message_content=True,
                guild_messages=True,
                members=True
            ),
            command_sync_flags=CommandSyncFlags(
                allow_command_deletion=True,
                sync_commands=True
            ),
            activity=Activity(
                name="in Elupiss",
                type=ActivityType.playing
            )
        )

    async def start(self, token: str) -> None:
        self.start_time = datetime.datetime.now()
        LOG.info("Starting Kerrik...")
        return await super().start(token)
