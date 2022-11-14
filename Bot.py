# bot.py
import os
import discord
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()

# 2
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.content == "!hola":
        await message.channel.send("Buenos dias!")


bot.run('MTA0MDE4NDQ2MTk0MzM4MjAyNg.Guovj4.1ZQgd_KjhYtN4l0umnP2rdbwZYoilRGTC63YO0')