# YouTube Bot

![](https://cdn.discordapp.com/attachments/815418855832551444/938217748314619934/image_2022-02-01_161812-removebg-preview_2.png)

![](https://img.shields.io/github/stars/Riceblade/YouTube-Discord-Bot.svg) ![](https://img.shields.io/github/forks/Riceblade/YouTube-Discord-Bot.svg) ![](https://img.shields.io/github/release/Riceblade/YouTube-Discord-Bot.svg) ![](https://img.shields.io/github/issues/Riceblade/YouTube-Discord-Bot.svg)

### Info

- YouTube Bot is a discord bot where you can search for anything on YouTube, it will automatically find the first result, the channel and a lot more info about it then format it into an embed, and if you would like there is a dropdown menu where you can make the bot send you an ephemeral message with the video as an embed to watch.

##Set-Up

###Required
- Code Text Editor e.g. [VSC](https://code.visualstudio.com/download) (visual studio code)
- [Python 3.9.10](https://www.python.org/downloads/release/python-3910/)
- [Google API Key](https://developers.google.com/youtube/v3/getting-started)
- Your Discord Bot [Token](https://discord.com/developers/applications)
####Enable YouTube API 
- [LINK](https://developers.google.com/youtube/v3)
###Adding Your Info
- Get your previously mentioned "Discord Bot Token" and replace the "bottokenhere" with your discord bot token.
- Found here
```python
cmd.run('tokenhere')
```
- Replace the "googleapikeyhere" found on line 18 with your Google API key
```python
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'googleapikeyhere'
```
- Now pip install all the modules and you are ready to run your bot!
- You can also host this bot
##Customizability
###Status
- To customize your bots status edit the information on line 13
```python
    await cmd.change_presence(activity=discord.Activity(name='😼😼😼😼😼', type=5))
```
- Name is the text that shows up in the status
- The type is what it says before that, e.g. "Streaming", "Listening to" or in this case "Competing in"
- Here are some types you can set it as:

| ID  | Name  | Format | Example |
| :------------: |:---------------:| :-----:| :-------:|
| 0 | Game | Playing {name} | "Playing Rocket League"
| 1 | Streaming |  Streaming {details} | "Streaming Rocket League"
| 2 | Listening	| Listening to {name} | "Listening to Spotify"
| 3 | Watching | Watching {name} | "Watching YouTube Together"
| 4 | Custom | {emoji} {name} | ":smiley: I am cool"
| 5 | Competing | Competing in {name} | "Competing in Arena World Champions"
###Search Info
- You can customize the search settings by editing the info found in lines 62-68
```python
    request = youtube.search().list(
        part="id,snippet",
        type='video',
        q=f"{output}",
        videoDuration='short',
        videoDefinition='high',
        maxResults=1,
        fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
    )
```
###Other
- and of course you can customize the embed and drop down menu
##How It Works

```flow
stt=>start: error
st=>start: Discord Command
op=>operation: Google API
cond=>condition: Request Successful Yes or No?
e=>operation: Check channel info
h=>end: Discord Embed

st->op->cond
cond(yes)->e->h
cond(no)->stt
```
###FAQ
- How do I avoid maxing out my quota on Googles API?
> You should add a cooldown to the bots commands, and if you are using this bot in a lot of servers I would recommend making more Google projects, getting the API keys from those, then using code that will randomly pick from 1 of up to 15 API keys in a text file.
- How can I host this bot without paying?
> I would recommend EC2 on AWS for free hosting, you can research how to use that, I am not typing out a tutorial because I am not in the mood to write a 30 page essay.
- Why did you waste so much time on the README.md?
>shut up.


#End
To reach me if you have any issues, or need help my discord is: Rice#0404.
