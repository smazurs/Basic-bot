import discord, os, datetime
import discord.ext
from dotenv import load_dotenv
from discord.ext import tasks, commands
from discord import Intents, Client, Message
from responses import get_response

# LOAD TOKEN TO ENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
intents.members = True # NOQA
client: Client = Client(intents=intents)
launch_time = datetime.datetime.utcnow()
bot = commands.Bot(command_prefix='$', intents=intents)

# HANDLING THE STARTUP & BOT STATUS

@client.event
async def on_ready():
  print(f'{client.user} is now running!')
  print(launch_time)
  if not Status_loop.is_running():
     Status_loop.start()

# BOT UPTIME
@tasks.loop(seconds=1, count=None, reconnect=True)
async def Status_loop():
  delta_uptime = datetime.datetime.utcnow() - launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)
  await client.change_presence(status = discord.Status.online,
    activity = discord.Activity(type=discord.ActivityType.playing,
    name = "Chess.com",
    state = f"{days:02d}d | {hours:02d}h | {minutes:02d}m Elapsed"))

# MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    if message.content:
        await send_message(message, user_message)

# MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
