import discord

bot = discord.bot()

TOKEN="ここにボットのトークンを張り付けてください"

@bot.command(description="テストコマンド")
async def test(ctx):
    await ctx.respond("hello world!")

@bot.event
async def on_ready():
    print("ボットがログインしました!")

bot.run(TOKEN)