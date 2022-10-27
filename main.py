import nextcord 
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def  on_ready():
    print ("The bot is now ready to use")


testingServerID = 1030827803022733414
@client.slash_command(name = "hello", description="Replies with hello", guild_ids=[testingServerID] )
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("Hello")


   


client.run('MTAzMDgyNzgwMzAyMjczMzQxNA.G8ae2Z.t2q_WiKY_nXWa8XtBn5PH3Q0zp_Kr7OUFXOY0o')

