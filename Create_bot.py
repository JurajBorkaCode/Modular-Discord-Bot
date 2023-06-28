import os
import sys

if len(sys.argv) > 1:
    bot_code = sys.argv[1]
else:
    print("Input your bot code in the format: Python Create_bot.py BOT_CODE")




startCode = '''
import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
'''

endCode = '''
bot.run('DISCORD_BOT_CODE')
'''

endCode = endCode.replace("DISCORD_BOT_CODE", bot_code)

module_folder = "Modules"
module_names = os.listdir(module_folder)

module_names.remove('__pycache__')

module_code = []

for module in module_names:
    with open("Modules/"+module,"r") as file:
        module_code.append(file.read())

created_bot_file = "Main_Bot.py"

with open(created_bot_file, "w") as file:
    file.write(startCode)
    for module in module_code:
        file.write("\n")
        file.write(module)
    file.write("\n")
    file.write(endCode)