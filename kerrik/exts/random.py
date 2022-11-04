from typing import Optional
from pydris import Extension, Message, param, StringParser
from random import randint
from kerrik.bot import Kerrik

ext = Extension("random", "The most randomest shit you never asked for.")


@param("user", StringParser(), required=False, default=None)
@ext.command(
    description="See how much bullshit that you or another person are spewing.",
    aliases=["howbs", "bs-o-metre", "bsmetre", "bs-metre"]
)
async def bs(client: Kerrik, msg: Message, user: Optional[str]):
    bs_metre = randint(0, 100)
    if not user:
        user = f"**{msg.author}**"
    else:
        user = f"**{user}**"
    responses = {
        0: f"{user}'s a fucking saint.",
        50: f"Something tells me that {user} is full of bullshit but are bullshitting about it.",
        75: f"{user} lives off of bullshit, {user} is full of shit, everything {user} utters is bullshit."
    }
    for k, v in responses.items():
        if bs_metre >= 75:
            return await client.send(f"**{bs_metre}%** {responses[75]}")
        elif bs_metre >= 50 and bs_metre < 75:
            return await client.send(f"**{bs_metre}%** {responses[50]}")
        elif bs_metre >= 0 and bs_metre < 50:
            return await client.send(f"**{bs_metre}%** {responses[0]}")
