import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('frank'):
            await message.reply('enstein')


# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run('MTE1NDgzOTMyMjIzOTk3OTY1MQ.Gt16FU.mO7P7WQxz-loe8efDoVDmsWcXBm3HCSkwLm29Y')