
# This example requires the 'members' privileged intents
import random

import nextcord
from nextcord.ext import commands

description = """An example bot to showcase the nextcord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
     await ctx.reply('pong')

bot.run("MTAzMDc3NDcyNTA4NzA4MDUyOQ.GNnpUI.iAah74M2uYYUZJuGZcP-lXa6CovU2yCifBEMTY")