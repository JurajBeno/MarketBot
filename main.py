from discord.ext import commands

from cogs.Csgo_market import CsgoMarketCog

TOKEN = "MTA2NTc0NTIzOTY2NDUwMDg0Ng.G3ljtb.f3beHyRlVeNsuWzfdqN7rkKAnfltK4li_WP5Vw"
DESC = "don't hate on me"

class MarketBot(commands.Bot):
    def __init__(self, command_prefix: str) -> None:
        commands.Bot.__init__(self, command_prefix=command_prefix, 
                              description=DESC)
        #todo
        self.add_cog(CsgoMarketCog(self))

    async def on_ready(self) -> None:
        print("BOT IS READY")


def main() -> None:
    client = MarketBot(command_prefix='>')
    client.run(TOKEN)


if __name__ == "__main__":
    main()