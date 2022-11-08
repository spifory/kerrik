from disnake.ext import plugins, commands
from typing import Optional
from disnake import Embed, Colour
from kerrik.bot import Kerrik


plugin = plugins.Plugin[Kerrik]()


@plugin.command(
    description="Get help with some stuff ig",
    usage="[command]"
)
async def help(ctx: commands.Context, command: Optional[str] = None):
    help_embed = Embed(colour=Colour.og_blurple())
    help_embed.title = "h"
    help_embed.description = ",".join([f"`{c.name}`" for c in plugin.bot.commands])
    help_embed.set_footer(
        text="Rember to not type out the [] or <>. [] just means optional, <> means required."
    )
    if command is not None:
        cmd = plugin.bot.get_command(command)
        if cmd is not None:
            help_embed.description = cmd.description
            help_embed.title = cmd.usage
            if cmd.aliases:
                help_embed.add_field("Aliases", ", ".join([f"`{c}`" for c in cmd.aliases]))

    await ctx.reply(embed=help_embed)

setup, teardown = plugin.create_extension_handlers()
