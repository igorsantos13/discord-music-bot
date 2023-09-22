import discord
from discord.ext import commands
import os

from dotenv import load_dotenv

load_dotenv()

#import all cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents=intents) 

#removes the default help command so we can create our own
bot.remove_command('help')

#register the class with the bot
@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))

class MyClient(discord.Client):
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('aaa'):
            await message.reply('bbb')

#start the bot with token
# bot.run(os.getenv("TOKEN"))
bot.run("MTE1NDgzOTMyMjIzOTk3OTY1MQ.Gt16FU.mO7P7WQxz-loe8efDoVDmsWcXBm3HCSkwLm29Y")