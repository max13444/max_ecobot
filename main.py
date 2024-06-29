import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

eco = ["Reduce, reuse, and recycle: Encourage recycling at home and school, and reduce waste by using reusable items like water bottles and bags",
        "Conserve energy: Turn off lights and electronics when not in use, unplug chargers, and use energy-efficient appliances",
        "Use sustainable transportation: Walk, bike, carpool, or take public transportation to reduce carbon emissions",
        "Support local and organic products: Buy locally grown and organic foods to reduce the carbon footprint associated with transportation and pesticides",
        "Plant trees and gardens: Participate in tree-planting events or start a garden to improve air quality and provide habitats for wildlife",
        "Volunteer: Get involved in environmental organizations or participate in beach clean-ups, park restorations, or other community projects"]

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#@bot.command()
#async def mem(ctx):
#   img_name = random.choice(os.listdir("images"))
#    with open(f'images/{img_name}', 'rb') as f:
#        picture = discord.File(f)
#    await ctx.send(file=picture)

@bot.command()
async def ecohelp(ctx):
    await ctx.send("Доступные команды: \n"
                   "facts - выводит количество доступных фактов. \n"
                   "ecofact - выводит случайный факт. \n"
                   "ecofact # - выводит факт с заданным # или случайный факт, если такого # нет.\n"
                   "ecohelp - эта команда.")



@bot.command()
async def facts(ctx):
    await ctx.send(f"в вашем распоряжении - {len(eco)} - фактов")

@bot.command()
async def ecofact(ctx, eco_index = -1):
    if eco_index < 0 or eco_index >= len(eco): 
        await ctx.send(f"Random fact - {random.choice(eco)}")
    else:
        await ctx.send(f"Fact #{eco_index} - {eco[eco_index]}")   

bot.run("insert token from the local file")