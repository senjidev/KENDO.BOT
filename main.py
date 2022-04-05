"""IMPORTS"""
import discord
from discord.ext import commands
import asyncio as a

"""VARIABLES"""
token_id = open('./token_/token.txt', 'r').read()
client = commands.Bot(command_prefix='/')
clientINS = discord.Client()


"""BOT LOGIN CONFIRMATION MESSEGE"""
@client.event
async def on_ready():
    await a.sleep(2)
    print('█████████████████████████████████████████████████████\n█▄─█─▄█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀█─▄▄─█████▄─▄─▀█─▄▄─█─▄─▄─█\n██─▄▀███─▄█▀██─█▄▀─███─██─█─██─█░░███─▄─▀█─██─███─███\n▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀')
    await a.sleep(2)
    print('\n developed by senji')

"""VIEW POST BOARD"""
@client.command(name='pb')
async def p_board(ctx):
    with open('./post_board/pb_banner.md', 'r') as banner:
        bnnr = banner.read()
        await ctx.send(bnnr)
    with open('./post_board/board01.md', 'r') as f: 
        scribe = f.read()
        await ctx.send(scribe)

"""PURGE MESSAGES"""
@client.command(name='rm')
@commands.has_permissions(administrator=True)
async def rm(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

client.run(token_id)