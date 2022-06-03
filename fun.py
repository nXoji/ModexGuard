import random
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        x = random.randint(0, 1)
        if x == 0:
            value = 'Монетка летит... Выпадает **Орёл**'
        if x == 1:
            value = 'Монетка летит... Выпадает **Решка**'

        embed = discord.Embed(
            description=value,
            color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command(aliases=['howdy', 'howdyho'])
    async def _howdy(self, ctx):
        imgUrl = [ "https://i.ibb.co/Rykx1ZJ/1.png", "https://i.ibb.co/FWqhmy5/2.jpg", "https://i.ibb.co/phhGPhk/3.jpg",
        "https://i.ibb.co/WnDD1z7/4.jpg", "https://i.ibb.co/pX63w3Q/5.jpg", "https://i.ibb.co/tQh4Gx5/image.jpg",
        "https://i.ibb.co/Jqwyr5Y/9.png", "https://i.ibb.co/nf4VF9J/8.png", "https://i.ibb.co/J5qyBqY/7.png",
        "https://i.ibb.co/gMw4ss5/6.png"]

        emb = discord.Embed(title = "Howdy Ho", color=ctx.author.color)
        emb.set_image(url = random.choice(imgUrl))
        await ctx.send(embed = emb)