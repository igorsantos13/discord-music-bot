import discord
from discord.ext import commands
import os

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

        if message.content.startswith('Bom dia'):
            await message.reply('BOM DIA!')

#start the bot with token
TOKEN = os.getenv("TOKEN") or ""
bot.run(TOKEN)