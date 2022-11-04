import datetime
from logging import getLogger
from pydris.client import Client

LOG = getLogger(__name__)


class Kerrik(Client):
    def __init__(self):
        self.start_time: datetime.datetime
        super().__init__("Kerrik", prefix="-")

    async def start(self) -> None:
        self.start_time = datetime.datetime.now()
        LOG.info("Starting Kerrik...")
        return await super().start()
