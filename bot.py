import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

# https://discord.com/api/oauth2/authorize?client_id=824410926937407529&permissions=387136&scope=bot

def get_prefix(bot,message):
    prefixes = ['.gacha ']
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user} in {len(bot.guilds)} servers.")

    
    await bot.change_presence(activity=discord.Activity(
        name="Genshin Impact",
        state="Spending Primogems"
        )
    )

modules = [
    "wish",
    "help"
]

for module in modules:
    bot.load_extension(f"cogs.{module}")

bot.run(os.getenv("BOT_TOKEN"))
