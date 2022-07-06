from ssl import OP_NO_COMPRESSION
import discord
import random
import requests
import urllib3
import re
import praw
from discord.ext import commands
#important codes

reddit = praw.Reddit(
    client_id="o_AU_eEcaIF1-_mNKTJ81A",
    client_secret="yDMxSj8g3v-IG6SOeV6k4arHwJkCrw",
    user_agent="discord bot",    
)

TOKEN = 'OTk0MDY4ODMzNzUxMDIzNzE2.Gqy4Ii.DrHpB8vCKPDWOu9Qs4Uho8UUPPJAHE5YpNrZaw'

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
            sub = reddit.subreddit('rarepuppers')
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            strForm = "{}".format(random_post.url)
            if 'v.redd.it' or 'gallery' in random_post.url:
              random_post_number = random.randint(0, 250)
              random_post = posts[random_post_number]
              strForm = "{}".format(random_post.url)
              await message.channel.send(random_post.url)
              return
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!cat':
            sub = reddit.subreddit('catpictures')
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            strForm = "{}".format(random_post.url)
            if 'v.redd.it' or 'gallery' in random_post.url:
              random_post_number = random.randint(0, 250)
              random_post = posts[random_post_number]
              strForm = "{}".format(random_post.url)
              await message.channel.send(random_post.url)
              return
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!bunny':
            sub = reddit.subreddit('bunnyflops')
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            strForm = "{}".format(random_post.url)
            if 'v.redd.it' or 'gallery' in random_post.url:
              random_post_number = random.randint(0, 250)
              random_post = posts[random_post_number]
              strForm = "{}".format(random_post.url)
              await message.channel.send(random_post.url)
              return
            await message.channel.send(random_post.url)
            return
        elif user_message.lower() == '!random':
            list = ['bunnyflops', 'catpictures', 'rarepuppers', 'aww', 'awww']
            random_sub = random.choice(list)
            sub = reddit.subreddit(random_sub)
            posts = [post for post in sub.hot(limit=250)]
            random_post_number = random.randint(0, 250)
            random_post = posts[random_post_number]
            strForm = "{}".format(random_post.url)
            if 'v.redd.it' or 'gallery' in random_post.url:
              random_post_number = random.randint(0, 250)
              random_post = posts[random_post_number]
              strForm = "{}".format(random_post.url)
              await message.channel.send(random_post.url)
              return
            else: 
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
            await message.channel.send(f'**!dog**: Get a photo of a cute doggo! \n **!cat**: Get a photo of a cute cat \n **!bunny**: Get a photo of a cute bunny! \n **!horse**: Get a photo of a cute horse! \n **!random**, Get a photo of a random animal!')
            return      
client.run(TOKEN)