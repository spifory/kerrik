import datetime
from logging import getLogger
from eludris.ext.commands import Bot

LOG = getLogger(__name__)


class Kerrik(Bot):
    def __init__(self):
        self.start_time: datetime.datetime
        super().__init__("Kerrik", "-")

    async def run(self) -> None:
        self.start_time = datetime.datetime.now()
        LOG.info("Starting Kerrik...")
        return await super().run()
