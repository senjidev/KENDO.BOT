"""IMPORTS"""
import discord
from discord.ext import commands
import asyncio as a
import time as t
"""VARIABLES"""
token_id = open('../KBtoken/token.txt', 'r').read()
client = commands.Bot(command_prefix='/')
clientINS = discord.Client()
global now
now = t.localtime()
global current_time
current_time = t.strftime("%m/%d %H:%M", now)

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
    with open("./commands.md", "r") as c:
        cmd_scribe = str(c.read())
    await ctx.send(cmd_scribe)

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
                scribe = str(f"\n```***{current_time}***\n{p2b.content}\n```\n ``` post by {p2b.author} in {p2b.guild}```") 
                await ctx.send(f"This post looking good?\n\n{scribe}")
                await a.sleep(1)
                await ctx.send("\n(Yes, or no)")
                def y_n_check(msg_y_n):
                    return msg_y_n.author == ctx.author and msg_y_n.channel == ctx.channel and msg_y_n.content.lower() in ["yes", "no"]
                m_y_n = await client.wait_for("message", check = y_n_check)
                if m_y_n.content.lower() == "yes":
                    f.write(str(f"\n***{current_time}***\n```{p2b.content}\n```\n ``` post by {p2b.author} in {p2b.guild}```"))
                    await ctx.send("Done! :)")
                else:
                    await ctx.send("oh well, doin' it anyway. >:)")
                    f.write(str(f"\n***{current_time}***\n```{p2b.content}\n```\n ``` post by {p2b.author} in {p2b.guild}```"))
    if m.content.lower() == "view":
        await p_board(m.channel)



"""WATCH PARTY INTEGRATION"""

@client.command(name='wp')
async def watch_party(ctx):
        await ctx.send("Would you like to schedule a new watch party event or view established ones?")
        await a.sleep(1)
        await ctx.send("Sch/View")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ["sch","view"]
        m = await client.wait_for("message", check =check)
        
        if m.content.lower() == "sch":
            await ctx.send("Go ahead and layout your schedule down there, and ill add it to the watch party board.")
            await a.sleep(.5)
            await ctx.send("If you would like an example on how i think you could format one best, type /wp_hlp")
            await a.sleep(.5)
            await ctx.send('Please rememeber to start your post with a "w^". Makes things easier for me to read. ;)')
            def wp_check(sch):
                return sch.author == ctx.author and sch.channel == ctx.channel
            wp2b = await client.wait_for("message", check =wp_check)

            if wp2b.content.startswith("w^"):
                with open('./wp/wp_board01.md', 'a') as wp_scribe:
                    wpScribe = f"\n***{current_time}***\n```{wp2b.content}\n\n***post by {wp2b.author} in {ctx.guild}***```\n"
                    await ctx.send("This schedule post look all good?\n")
                    await ctx.send(str(wpScribe))
                    await a.sleep(1)
                    await ctx.send("Yes or no?\n")
                    def wp_y_n(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["yes", "no"]
                    wp2b_fin = await client.wait_for("message", check =wp_y_n)
                    if wp2b_fin.content.lower() == "yes":
                        await ctx.send(f"Creating your schedule {wp2b.author}!\n")
                        wp_scribe.write(str(f"\n***{current_time}***\n```{wp2b.content}\n\n***post by {wp2b.author} in {ctx.guild}***```"))
                        await a.sleep(2)
                        await ctx.send("Done!\n")

                    if wp2b_fin.content.lower() == "no":
                        await ctx.send(f"The edit post feature is currently under development. :((( \n ***FUTURE FEATURE WILL INCLUDE THIS.\n DO NOT TRY ANSWERING THIS PART OF THE QUESTION.\n THE COMMAND REACHED AN EXCEPTION AND HAS EXITED PLEASE RUN THIS COMMAND AGAIN WITH YOUR EDITED POST***\n(Would you like to post this schedule anyway, or discard it?)")
                        #add conditionals here

        if m.content.lower() == "view":
            with open('./wp/wp_board01.md', 'r') as f:
                scribe = f.read()
                await ctx.send(str(f'\n{scribe}\n'))

"""API INTEGRATIONS"""

 

"""BOT DESCRIPTION"""
@client.command(name="bio")
async def tell_me_about_yourself(ctx):
    text = f'My name is {client.user}!\n I was built by senji. At present I have limited features(find out more by typing "/hlp")\n :)'
    await ctx.send(text)






client.run(token_id)
