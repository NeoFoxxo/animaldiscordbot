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

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'wasup {username}!')
            return
        elif user_message.lower() == '!dog':
            message1 = await message.channel.send(f'One cute dog coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            sub = reddit.subreddit('rarepuppers')
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            if random_post.is_video:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif random_post_number == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!cat':
            message1 = await message.channel.send(f'One cute cat coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            sub = reddit.subreddit('catpictures')
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.choice(range (0, 250))
            random_post = posts[random_post_number]
            if random_post.is_video:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif random_post_number == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
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
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            if random_post.is_video:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif random_post_number == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!random':
            message1 = await message.channel.send(f'One cute animal coming up {username}!')
            message2 = await message.channel.send(f'https://user-images.githubusercontent.com/3053271/32455273-6118a5fc-c2e7-11e7-8265-9829b231be4d.gif')
            list = ['bunnyflops', 'catpictures', 'rarepuppers', 'aww', 'awww']
            random_sub = random.choice(list)
            sub = reddit.subreddit(random_sub)
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            if random_post.is_video:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            elif random_post_number == 14:
                await message1.delete()
                await message2.delete()
                await message.channel.send(f'https://cdn.discordapp.com/attachments/461799833540231170/994573993355001856/6m1k6j.jpg')
            elif 'gallery_data' in random_post.__dict__:
              random_post_number = random.choice(range (0, 250))
              random_post = posts[random_post_number]
              await message1.delete()
              await message2.delete()
              await message.channel.send(random_post.url)
              return
            await message1.delete()
            await message2.delete()
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!horse':
            await message.channel.send(f'no horses for you {username}!')
            return

        #elif user_message.lower() == '!help':
            async def embed(ctx):
                embed=discord.Embed(
                title="Commands",
                    description="Here are the all commands and what they do",
                    color=discord.Color.blue())
                embed.add_field(name="**!dog**", value="Get a photo of a cute doggo!", inline=False)
                embed.add_field(name="**!cat**", value="Get a photo of a cute cat!", inline=False)
                embed.add_field(name="**!bunny**", value="Get a photo of a cute bunny!", inline=False)
                embed.add_field(name="**!horse**", value="Get a photo of a cute horse!", inline=False)
                embed.add_field(name="**!random**", value="Get a photo of a random animal!", inline=False)
                await ctx.send(embed=embed)
                return
        elif user_message.lower() == '!guide':
            await message.channel.send(f'**!dog**: Get a photo of a cute doggo! \n**!cat**: Get a photo of a cute cat! \n**!bunny**: Get a photo of a cute bunny! \n**!horse**: Get a photo of a cute horse! \n**!random**: Get a photo of a random animal!')
            return      
client.run(TOKEN)