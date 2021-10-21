from discord.ext import commands
from discord import Embed
from banners import available_banners

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        embed = Embed(title="Gacha Bot", description="\u200b", color=0x2aec27)
        embed.add_field(name=".gacha wish [banner] [rolls]",value="**banner**: Required argument specifying which banner. \n**rolls**: Defaults to 1 and cannot exceed 10.",inline=False)
        
        banners = ""
        for entry in available_banners:
            banners += entry + "\n"
        
        embed.add_field(name="Available Banners",value=banners)
        embed.set_footer(text="Gacha Bot by Over#6203.")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/gensin-impact/images/1/1f/Item_Intertwined_Fate.png/revision/latest/top-crop/width/360/height/360?cb=20201117073436")
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))