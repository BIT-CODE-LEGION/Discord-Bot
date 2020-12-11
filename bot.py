import discord
from discord.ext import commands
import csv
from itertools import cycle
import os
import sys
import datetime
from time import sleep
from io import StringIO
from datetime import datetime 

prefix = '>'
token = 'NjkwMDE4MDY3MjQ1NDMyODgy.XnLTZw.PiWPVvNyrj9iBR5xN6mCV9yKGbM'

client = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('<------------------------------>')
    print('EPAX\'s Bot is ready')
    print(f'Using Discord.py Version {discord.__version__}')
    print('<------------------------------>')

    activity = discord.Activity(name='my DMs |  DM me to send Mod Mail', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

extensions = ['cogs.ModMail']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)

@client.event
async def on_connect():
    print('Connected to Discord')



    

def com_exec(com = ""):
	cout = StringIO()		#\
	old_out = sys.stdout	# > Save std out to var; to return/send back as discord msg
	sys.stdout = cout		#/

	try:
		exec(com)
	except:
		print(' '.join(str(stuff) for stuff in sys.exc_info()))
	res = cout.getvalue()
	
	sys.stdout = old_out	# reset std out
	cout.close()
	return(res)


@client.command()
async def run(ctx , *,script ):
    if 'import sys' in script:
        await ctx.send('```fix\n Sorry you cant import "sys" for system security```')
    elif 'import os' in script:
        await ctx.send('```fix\n Sorry you cant import "OS" for system security```')
    elif '```python' in  script :
        script = script[9:-3]
        
        try :
            res = com_exec(script)

            await ctx.send('```shell\n'+res+'```')
        except Exception as e :
            await ctx.send("```fix\n{}\n```".format(e))
    else :
        
        try :
            res = com_exec(script)

            await ctx.send('```fix\n'+res+ '```')
        except Exception as e :
            await ctx.send("```fix\n{}\n```".format(e))
    

# logger = getLogger(None)
# @client.event()
# async  def setup(ctx ):
#     if ctx.guild != bot.madmail_guild

@client.command()
async def serverlink(ctx ):
    em = discord.Embed( color = discord.Colour.blue())
    em.set_image( url = 'https://cdn.discordapp.com/attachments/722143176764162049/785913368153554974/giphy_1.gif')
    await ctx.send(embed= em)
    await ctx.send('https://discord.gg/SYjc9F2')


# @client.command()
# async def rules(ctx ):
#     em = discord.Embed( color = discord.Colour.blue())
#     em.set_image( url = 'https://media.discordapp.net/attachments/722143176764162049/785912103793459250/giphy.gif')
#     await ctx.send(embed= em)
#     em2 = discord.Embed( description ="""
#         To maintain this community's awesomeness, make sure you've read the rules and guidelines stated below:

# `❌` . Do not break Discord's Terms of Service in any channels.

# `❌` . Respect everyone in this server

# `❌` . Use the correct channels. They are split up for a reason.

# `❌` . Do not spam in any channel.

# `❌` . English is the primary language of the server. Use other languages in their respective channels.

# `❌` . Do not post other Discord links or unsolicited links in chat or in other peoples DMs. It is a bannable offense.

# `❌` . Sharing personal or confidential information about another user will lead to a ban.

# `❌` . Do not beg about or try to sell/buy any in-game item, money or otherwise in any chat or in DMs.

# `❌` . Server nicknames must contain a minimum of two characters, may not consist of only special characters, and must comply with other rules specified in this channel. The staff reserves the right to adjust server nicknames at their discretion. It is ultimately up to the staff whether to approve a nickname request.

# `❌` . If you feel unfairly judged by the Moderators, feel free to contact any Administrator for help. Do not squabble about it in chat.

# `❌` . Racism, sexism, sexually explicit or otherwise offensive content, politics/religion will not be tolerated. Nothing NSFW.

# `❌` . Do not impersonate any server members, especially staff.

# `❌` . Don't use toxic languages in any vc

# `❌` . Do not send visual content, such as emojis, pictures and videos, that cause epilepsy and/or seizure.

# `❌` . Do not antagonize or encourage users to violate the rules, or purposefully try to get a specific user punished.

# `❌` . Excessive usage of markdown text, especially codeblocks, is forbidden.

# `❌` . Conversations based on degrading race, nationality, religion, culture, gender, sexual preference are not allowed

    
    
#     """ ,color = discord.Colour.blue())
#     em2.set_image(url = 'https://imageshost.ru/images/2019/05/14/source.gif')
#     await ctx.send(embed= em2)
client.run(token)
