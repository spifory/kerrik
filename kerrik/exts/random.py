from typing import Optional
from disnake.ext import plugins, commands
from disnake import Member, Message, MessageType
from random import randint
from kerrik.bot import Kerrik

plugin = plugins.Plugin[Kerrik]()


@plugin.command(
    description="See how much bullshit that you or another person are spewing.",
    aliases=["howbs", "bs-o-metre", "bsmetre", "bs-metre"],
    usage="[user]"
)
async def bs(ctx: commands.Context[Kerrik], user: Optional[Member] = None):
    bs_metre = randint(0, 100)
    if user is None:
        user = f"**{ctx.author}**"
    else:
        user = f"**{user}**"

    if ctx.message.reference is not None:
        user = f"**{ctx.message.reference.resolved.author}**"

    responses = {
        0: f"{user}'s a fucking saint.",
        50: f"Something tells me that {user} is full of bullshit but are bullshitting about it.",
        75: f"{user} lives off of bullshit, {user} is full of shit, everything {user} utters is bullshit."
    }
    for k, v in responses.items():
        if bs_metre >= 75:
            return await ctx.reply(f"**{bs_metre}%** {responses[75]}")
        elif bs_metre >= 50 and bs_metre < 75:
            return await ctx.reply(f"**{bs_metre}%** {responses[50]}")
        elif bs_metre >= 0 and bs_metre < 50:
            return await ctx.reply(f"**{bs_metre}%** {responses[0]}")


PEOPLE = {
    256133489454350345: "<:woo:1012378275538018405>",
    716134528409665586: "shut up",
    559226493553737740: "clown talking lmfao",
    484541026636136449: "send regex",
    756258832526868541: "what a <@756258832526868541>e",
    305017820775710720: "no one ever listens to what you say btw"
}


@plugin.listener("on_message")
async def reply_thing(message: Message):

    if message.type == MessageType.reply:
        if message.reference.resolved.author.id == plugin.bot.user.id:  # type: ignore
            await message.reply(PEOPLE[message.author.id].format(sham=message.author.mention))

setup, teardown = plugin.create_extension_handlers()
