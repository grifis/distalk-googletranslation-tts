import discord
from discord.ext import commands
import asyncio
import os
import subprocess
from gtts import gTTS

client = commands.Bot(command_prefix='.')
voice_client = None
channel_id = None

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def join(ctx):
    print('#voicechannelを取得')
    vc = ctx.author.voice.channel
    global channel_id
    channel_id = ctx.channel.id
    print(f'{channel_id}')
    print('#voicechannelに接続')
    await vc.connect()

@client.command()
async def bye(ctx):
    print('#切断')
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message):
    if message.channel.id != channel_id:
        pass
    else:
        msgclient = message.guild.voice_client
        if message.content.startswith('?'):
            pass

        else:
            if message.guild.voice_client:
                print(message.content)
                myText = "おはようございます"
                language = 'ja'
                output = gTTS(text=message.content, lang=language, slow=False)
                output.save("output.mp3")
                source = discord.FFmpegPCMAudio("output.mp3")
                message.guild.voice_client.play(source)
            else:
                pass
    await client.process_commands(message)


client.run("NzYzNDI0NDE0ODUwNjEzMjQ5.X33gZA.GpcDgThL-h4zEW1BkG5xilmMbSA")