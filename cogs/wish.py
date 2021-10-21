import discord
from discord.ext import commands
from banners import available_banners

class Wish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wish")
    async def do_wish(self, ctx, banner, *quantity):
        if banner.lower() in available_banners:
            banner = available_banners[banner.lower()]()
        else:
            await ctx.reply(f"Banner `{banner} not available.`")
            return
        
        # Initializes banner class with the user and wishes
        banner.user = ctx.author.id
        banner.get_user()
        if quantity:
            try:
                quantity = abs(round(float(quantity[0])))
            except:
                quantity = 1
            if quantity > 10:
                quantity = 10
        else:
            quantity = 1
        
        banner.do_many_wishes(quantity)

        # Initializes reaction menu
        output = await ctx.reply(embed=banner.embed_list[0])
        await output.add_reaction("⏮")
        await output.add_reaction("◀️")
        await output.add_reaction("▶️")
        await output.add_reaction("⏭")

        # Check for the reaction menu
        def check(reaction, user):
            # Ensures that the reaction is from the author and on the output message
            return user == ctx.author and reaction.message.id == output.id

        pages = len(banner.embed_list)
        current_page = 1
        reaction = None

        while True:
            if str(reaction) == "⏮":
                current_page = 1
                await output.edit(embed=banner.embed_list[current_page-1])
            
            elif str(reaction) == "▶️" and current_page != pages:
                current_page += 1
                await output.edit(embed=banner.embed_list[current_page-1])

            elif str(reaction) == "◀️" and current_page > 1:
                current_page -= 1
                await output.edit(embed=banner.embed_list[current_page-1])
            
            elif str(reaction) == "⏭":
                current_page = pages
                await output.edit(embed=banner.embed_list[current_page-1])
     
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                await output.remove_reaction(reaction, user)
            except:
                break

        await output.clear_reactions()
        await output.edit(embed=banner.embed_list[-1])



def setup(bot):
    bot.add_cog(Wish(bot))