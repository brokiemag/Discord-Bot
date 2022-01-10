# Discord-Bot 

Discord bots are AIs that can perform a number of useful automated tasks and bot commands on your server, such as welcoming new members, moderating content, and banning rule breakers. You can use bot commands to add music, memes, games, and other content to your server.

## Installation

Use the package manager [pip](https://pypi.org/project/pip/) to install -r requirements.txt .

```bash
pip install -r requirements.txt
```

## Usage

```python
from discord_webhook import DiscordWebhook
import discord 

client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

if msg.startswith(".hello"):
    await message.channel.send("Hi I am a BOT i can do anything , please type .help for the list of commands.")
  if msg.startswith(".hi"):
    await message.channel.send("Hi I am a BOT i can do anything , please type .help for the list of commands.")

client.run("KEy#")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://brokiemag.me)
