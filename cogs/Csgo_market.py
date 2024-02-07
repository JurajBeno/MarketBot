from discord.ext import commands, tasks
from discord import Embed, Color


import sys
 
# setting path
sys.path.append('../cases_bot')
from util.Funnel import FunnelToCog

class CsgoMarketCog(commands.Cog):
    time_of_case = 0
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.funnel = FunnelToCog()
        self.channel_to_post = 0

    @commands.command(name="csgocases", help="will check prices of items on steam market place of Cases in xlsx file named MojeCasky.xlsx and post embed with all info of every case every given time (in minutes) or every hour syntax: >csgocases <time>")
    async def start_cases(self, ctx: commands.Context, time_in_min: int=60) -> None:
        if self.channel_to_post == ctx.channel.id:
            await ctx.send(embed=Embed(title="CHANNEL ALREADY ASSIGNED TO RECIVE UPDATES ON CASES"))
        self.channel_to_post = ctx.channel.id
        self.time_of_case = time_in_min
        await ctx.send(embed=Embed(title="CHANNEL REGISTERED TO RECIVE UPDATES ON CASES", color=Color.green()))
        await self.send_embed_with_case.start()

    @commands.command(name="dissablecases", help="will dissable info about cases")
    async def disable_casses(self, ctx: commands.Context) -> None:
        self.channel_to_post = 0
        await ctx.send(embed=Embed(title="CHANNEL UNREGISTERED TO RECIVE INFO ON CASES", color=Color.green()))
        await self.send_embed_with_case.stop()

    @tasks.loop(minutes=15)
    async def send_embed_with_case(self) -> None:
        channel = self.bot.get_channel(id=self.channel_to_post)
        for i in range(0, self.funnel.xl.get_number_of_rows()):
            await channel.send(embed=self.create_case_embed(i))
        pass

    def create_case_embed(self, case_id) -> Embed:
        item = self.funnel.give_item(case_id)
        if item.market_price > item.my_sell_price:
            embed = Embed(title=item.name,
                          url=f"https://steamcommunity.com/market/listings/730/{item.hash_name}",
                          description="SELL NOW  SELL NOW  SELL NOW",
                          color=Color.red())
        else:
            embed = Embed(title=item.name,
                          url=f"https://steamcommunity.com/market/listings/730/{item.hash_name}",
                          description="ITEM ON MARKET IS DOING ACCORDING TO DETAILS:")
        embed.add_field(name=f"{item.my_sell_price} €", value="Price i am willing to sell at", inline=True)
        embed.add_field(name=f"{item.market_price} €", value="Current market price", inline=True)
        embed.add_field(name=f"{item.my_buy_price} €" , value="Price of last of type bought", inline=True)
        embed.add_field(name=item.my_quantity, value="Item quantity")
        embed.set_thumbnail(url=item.picture_link)
        return embed
