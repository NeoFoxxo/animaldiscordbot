from ssl import OP_NO_COMPRESSION
import discord
import random
import requests
import urllib3
import re
import praw
from discord.ext import commands

#important codes
with open('disc-token.txt', 'r') as f:
    tokendiscord = f.read()

with open('reddit-client-id.txt', 'r') as f:
    redditid = f.read()

with open('reddit-client-secret.txt', 'r') as f:
    redditsecret = f.read()

reddit = praw.Reddit(
    client_id=redditid,
    client_secret=redditsecret,
    user_agent="discord bot",
    check_for_async=False   
)

TOKEN = tokendiscord

client = discord.Client()

gallery = ('https://www.reddit.com/gallery/')
video = ('https://v.redd.it/')

#notification that the bot is online
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

#relay all messages to console
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    #only sends messages in general channel
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'wasup {username}!')
            return
        elif user_message.lower() == '!dog':
            message1 = await message.channel.send(f'One cute dog coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            sub = reddit.subreddit('rarepuppers')
            posts = [post for post in sub.hot(limit=250)]
            random_post = random.choice(posts)
            #funny easter egg
            depss = random.randint(0, 14)
            if depss == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
                return
            while video in random_post.url:
              random_post = random.choice(posts)
              if video not in random_post.url:
                await message1.delete()
                await message2.delete()
                await message.channel.send(random_post.url)
                break 
            while gallery in random_post.url:
              random_post = random.choice(posts)
              if gallery not in random_post.url:
                await message1.delete()
                await message2.delete()
                await message.channel.send(random_post.url)
                break 
            #else:  
                #await message1.delete()
                #await message2.delete()
                #await message.channel.send(random_post.url)
                #return
            #elif 'gallery_data' in random_post.__dict__:
              #random_post = random.choice(posts)
              #await message1.delete()
              #await message2.delete()
              #await message.channel.send(random_post.url)
              #return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!cat':
            message1 = await message.channel.send(f'One cute cat coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            sub = reddit.subreddit('catpictures')
            posts = [post for post in sub.hot(limit=250)]
            random_post = random.choice(posts)
            if random_post.is_video:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif depss == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!bunny':
            message1 = await message.channel.send(f'One cute bunny coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            sub = reddit.subreddit('bunnyflops')
            posts = [post for post in sub.hot(limit=250)]
            random_post = random.choice(posts)
            if random_post.is_video:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif depss == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        #find a post from a random subreddit in the list
        elif user_message.lower() == '!random':
            message1 = await message.channel.send(f'One cute animal coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            list = ['bunnyflops', 'catpictures', 'rarepuppers', 'aww', 'awww']
            random_sub = random.choice(list)
            sub = reddit.subreddit(random_sub)
            posts = [post for post in sub.hot(limit=250)]
            random_post = random.choice(posts)
            #if post is a video post find another post
            if random_post.is_video:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif depss == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            #if post is a gallery post find another post
            elif 'gallery_data' in random_post.__dict__:
              random_post = random.choice(posts)
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        #troll command lol
        elif user_message.lower() == '!horse':
            await message.channel.send(f'no horses for you {username}!')
            return
        #give a list of all commands
        elif message.content.startswith('!help'):
            embedvar=discord.Embed(title="Commands", description="Here are the all commands and what they do", color=discord.Color.blue())
            embedvar.add_field(name="**!dog**", value="Get a photo of a cute doggo!", inline=False)
            embedvar.add_field(name="**!cat**", value="Get a photo of a cute cat!", inline=False)
            embedvar.add_field(name="**!bunny**", value="Get a photo of a cute bunny!", inline=False)
            embedvar.add_field(name="**!horse**", value="Get a photo of a cute horse!", inline=False)
            embedvar.add_field(name="**!random**", value="Get a photo of a random animal!", inline=False)
            await message.channel.send(embed=embedvar)
            return     

client.run(TOKEN)