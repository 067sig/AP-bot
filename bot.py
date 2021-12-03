import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

@client.command()
async def ping(ctx):
    """Sends the latency"""
    await ctx.send(f' {round(client.latency * 1000)}ms')

@client.command()
async def echo(self, ctx, *, message=None):
    """
    A command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)

@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    memberAvatar = member.avatar_url

    avatarEmbed = discord.Embed(title=f"{member.name}'s Avatar")
    avatarEmbed.set_image(url = memberAvatar)

    await ctx.send(embed = avatarEmbed)

@client.command(aliases=['8ball'])
async def _8bal1(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    for i in range(amount): # Do the next thing amount times
        await ctx.send(message) # Sends message where command was called

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

token = ""
with open ("token.txt") as file:
    token = file.read()



client.run(token)