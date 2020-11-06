import dotenv
dotenv.load_dotenv(verbose=True)

import discord
from discord.ext import commands
import os
import chalk

from utils import config
from cogs import identities

bot = commands.Bot(os.getenv("bot_prefix"))
bot.remove_command('help')
cogs = []


def add_cog(cog):
    bot.add_cog(cog)
    cogs.append(cog)
    print(chalk.cyan(f"Loaded cog: {cog}"))

def register_cogs():
    print(chalk.yellow("Loading cogs..."))
    add_cog(identities.Identities(bot))

def start(token):
    register_cogs()
    print(chalk.yellow("Starting bot..."))
    bot.run(token)

@bot.event
async def on_connect():
    print(chalk.yellow("Connected to Discord servers..."))


@bot.event
async def on_ready():
    print(chalk.green("Identity is online."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f"with IDs", url="https://twitch.tv/Mahjestic"))


@bot.event
async def on_disconnect():
    print(chalk.red("Disconnected from Discord servers..."))


start(os.getenv("token"))