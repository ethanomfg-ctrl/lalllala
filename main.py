import discord

TOKEN = "MTUyMjM0NTUwNDcwMzM4MTc2NA.GpX4CN.bV3fAJYpqbpv3zVQL1tEXcI4rCSqhnsIi2iwws"

class Bot(discord.Client):
    async def on_ready(self):
        print("bot alive")

bot = Bot()
bot.run(TOKEN)
