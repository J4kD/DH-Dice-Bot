import os, random, re, math
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-')

@bot.command(name='-')
async def roll(context, *, arg):
    arg = arg.replace(" ", "")
    match = re.fullmatch(r"([+-]?[0-9]+)([+-][0-9]+)*", arg)
    if match is None:
        response = f"Sorry {context.author.display_name}, invalid command."
    else:
        target = sum(int(arg) for arg in match.groups() if arg is not None)
        roll = random.randint(1, 100)
        difference = target - roll
        if difference >= 0:
            degrees = math.ceil((difference + 1) / 10)
            if roll == 1:
                degrees += 1
        elif roll == 1:
            degrees = 1
        else:
            degrees = math.floor((difference - 1) / 10)
        response = f"{context.author.display_name} | Target: `{target}` Roll: `{roll}` Result: `{abs(degrees)} degree{'s' if abs(degrees) > 1 else ''} of {'success' if degrees > 0 else 'failure'}`"
    await context.send(response)

bot.run(TOKEN)
