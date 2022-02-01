import discord
import googleapiclient.discovery
from discord.ext import commands
import typing
from discord_ui import UI
cmd = commands.Bot(command_prefix='.')
client = discord.Client()


@cmd.event
async def on_ready():
    print('We have logged in as {0.user}'.format(cmd))
    await cmd.change_presence(activity=discord.Activity(name='😼😼😼😼😼', type=5))


api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'googleapikeyhere'
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)


@cmd.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f"You are on cooldown for {round(error.retry_after, 2)} seconds!")


@ cmd.command()
@ commands.cooldown(1, 4, commands.BucketType.user)
async def info(ctx, *args):
    output2 = ''
    for word in args:
        output2 += str(word)
        output2 += ' '
        print(output2)
    request3 = youtube.channels().list(
        part="snippet",
        id=f"{output2}",
    )
    response3 = request3.execute()
    print(response3)
    channame = response3['items'][0]['snippet']['title']
    icon = response3['items'][0]['snippet']['thumbnails']['default']['url']
    chanid = response3['etag']
    dsc = response3['items'][0]['snippet']['description']
    embed2 = discord.Embed(title=f"{channame}", url=f"https://www.youtube.com/watch?v={chanid}",
                          description=f"{dsc}", color=0xFF5733)
    response3 = request3.execute()
    embed2.add_field(text=f"Made By Riceblades11")
    await ctx.send(embed=embed2)


@ cmd.command()
@ commands.cooldown(1, 30, commands.BucketType.user)
async def search(ctx, *args):
    output = ''
    for word in args:
        output += str(word)
        output += ' '
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q=f"{output}",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1,
        fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
    )
    response = request.execute()
    chan = response['items'][0]['snippet']['channelId']
    title = response['items'][0]['snippet']['title']
    idd = response['items'][0]['id']['videoId']
    dsc = response['items'][0]['snippet']['description']
    embed = discord.Embed(title=f"{title}", url=f"https://www.youtube.com/watch?v={idd}",
                          description=f"{dsc}", color=0xFF5733)
    embed.set_image(
        url=f"https://i.ytimg.com/vi/{idd}/mqdefault.jpg")
    request2 = youtube.channels().list(
        part="snippet",
        id=f"{chan}",
    )
    response2 = request2.execute()
    pfp = response2['items'][0]['snippet']['thumbnails']['default']['url']
    name = response2['items'][0]['snippet']['localized']['title']
    embed.set_author(
        name=name, url=f"https://www.youtube.com/channel/{chan}", icon_url=pfp)
    embed.set_footer(text="Made By Riceblades11")
    view = DropdownView(idd)
    await ctx.send(embed=embed, view=view)


class Dropdown(discord.ui.Select):
    def __init__(self, idd):
        self.idd = idd
        options = [
            discord.SelectOption(
                label='Link', description='Click for YouTube Link', emoji='🟥'),

        ]
        super().__init__(placeholder='Pick Option',
                         min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Link: https://www.youtube.com/watch?v={self.idd}', ephemeral=True)


class DropdownView(discord.ui.View):
    def __init__(self, idd):
        super().__init__()
        self.add_item(Dropdown(idd))


cmd.run('bottokenhere')
