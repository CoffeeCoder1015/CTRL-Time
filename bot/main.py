# This example requires the 'message_content' intent.
from dotenv import load_dotenv
load_dotenv()
import os
import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        
        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)
        
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    
    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        print(message.author,self.user)
        if message.author == self.user:
            return
        await message.channel.send("Hello world!")
    
    async def setup_hook(self) -> None:
        await self.tree.sync()
        
client = MyClient()

@client.tree.command(description="Register for the service")
async def register(interaction: discord.Interaction, member: discord.Member):
    print(member.name,"Ran this command")
    await interaction.response.send_message(f"Hello {member.name}")

client.run(os.getenv("DISCORD_TOKEN"))