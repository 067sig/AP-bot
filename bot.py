import discord
from discord.ext import commands

client = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")



token = ""
with open ("token.txt") as file:
    token = file.read()



client.run(token)