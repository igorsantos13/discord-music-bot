import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
General commands:
/help - mostra os comandos.
/p <keywords> - procura a musica no youtube e começa a tocar.
/q - mostra a lista de musicas
/skip - pula a musica atual
/clear - limpaa fila de musicas e para a atual.
/leave - Desconecta o bot do canal.
/pause - Pausa a musica ou Despausa caso esteja pausada.
/resume - Despausa a musica.
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)