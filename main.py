"""IMPORTS"""
import discord
from discord.ext import commands
import asyncio as a
from datetime import datetime as dt
"""VARIABLES"""
token_id = open('../KBtoken/token.txt', 'r').read()
client = commands.Bot(command_prefix='/')
clientINS = discord.Client()
global now
now = dt.now()
global current_time
current_time = now.strftime("%m/%d %H:%M")

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

"""HELP COMMAND"""
@client.command(name='hlp')
@commands.has_permissions(administrator=True)
async def hlp(ctx):
    await ctx.send(
        f'Available Commands:\n\t(Post Board: "/pb" ***Displays The Post Board for events and activities***)\n\t(Bio: "/bio" ***Displays a brief description of KendoBot***)\n\t(Add To Post Board: "/addto" ***Allows a user to create a message and post it!***)'
        )

"""ADD TO POST BOARD FROM CLIENT?"""
@client.command(name='addto')
@commands.has_permissions(administrator=True)
async def addto(ctx):
    
    await ctx.send('Would you like to ***add***  a new post, or ***view***  previous ones?\n')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["add", "view"]    
    m = await client.wait_for("message", check=check)
    if m.content.lower() == "add":
        await ctx.send("Write out your post down there, and ill add it to the board. (Please Remember to add a '^' at the beginning of your post, makes it easier for me to read. ;)")
        
        def p2b_check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        p2b = await client.wait_for("message", check=p2b_check)
        
        if p2b.content.startswith("^"):
            with open('./post_board/board01.md', 'a') as f:
                scribe = str(f"\n```***{current_time}***\n{p2b.content}\n```\n ``` post by {p2b.author}```")
                await ctx.send(f"This post looking good?\n\n{scribe}")
                await a.sleep(1)
                await ctx.send("\n(Yes, or no)")
                def y_n_check(msg_y_n):
                    return msg_y_n.author == ctx.author and msg_y_n.channel == ctx.channel and msg_y_n.content.lower() in ["yes", "no"]
                m_y_n = await client.wait_for("message", check = y_n_check)
                if m_y_n.content.lower() == "yes":
                    f.write(str(f"\n***{current_time}***\n```{p2b.content}\n```\n ``` post by {p2b.author}```"))
                    await ctx.send("Done! :)")
                else:
                    await ctx.send("oh well, doin' it anyway. >:)")
                    f.write(str(f"\n***{current_time}***\n```{p2b.content}\n```\n ``` post by {p2b.author}```"))
    if m.content.lower() == "view":
        await p_board(m.channel)



"""WATCH PARTY INTEGRATION"""

@clientINS.event
async def on_message(message):
    if message.content.startswith('party/'):
        chnl = message.channel
        chnl.send("{WATCH PARTY SCHEDULE/INFO HERE}")



"""API INTEGRATIONS"""



"""BOT DESCRIPTION"""
@client.command(name="bio")
async def tell_me_about_yourself(ctx):
    text = f'My name is {client.user}!\n I was built by senji. At present I have limited features(find out more by typing "/hlp")\n :)'
    await ctx.send(text)






client.run(token_id)