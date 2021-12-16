import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord_webhook import DiscordWebhook
import wikipedia
from bs4 import BeautifulSoup
import time
import pyjokes
from datetime import date


client = discord.Client()
issuegen = str(random.random())
issuegenrep = issuegen.replace('0.','') 
sad_words = [".sad", ".depressing", ".unhappy", ".angry", ".miserable", ".depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person",
  "You are the best programmer"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('.weather'):
    api_key = "#yourkey"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" +"hyderabad"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":  
              y = x["main"] 

              # store the value corresponding 
              # to the "temp" key of y 
              current_temperature = y["temp"] 

              # store the value corresponding 
              # to the "pressure" key of y 
              current_pressure = y["pressure"] 

              # store the value corresponding 
              # to the "humidity" key of y 
              current_humidiy = y["humidity"] 

              # store the value of "weather" 
              # key in variable z 
              z = x["weather"] 

              # store the value corresponding  
              # to the "description" key at  
              # the 0th index of z 
              weather_description = z[0]["description"] 

              # print following values 
              await message.channel.send(" Temperature (in kelvin unit) = " +
                              str(current_temperature) + " atmospheric pressure (in hPa unit) = " +str      (current_pressure) +" humidity (in percentage) = " + str(current_humidiy) + "       description = " + str(weather_description)) 
  if msg.startswith('.temp'):
    api_key = "#Yourkey"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" +"#yourcity"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":  
              y = x["main"] 

              # store the value corresponding 
              # to the "temp" key of y 
              current_temperature = y["temp"] 

              # store the value corresponding 
              # to the "pressure" key of y 
              current_pressure = y["pressure"] 

              # store the value corresponding 
              # to the "humidity" key of y 
              current_humidiy = y["humidity"] 

              # store the value of "weather" 
              # key in variable z 
              z = x["weather"] 

              # store the value corresponding  
              # to the "description" key at  
              # the 0th index of z 
              weather_description = z[0]["description"] 

              # print following values 
              await message.channel.send(" Temperature (in kelvin unit) = " +
                              str(current_temperature) + " atmospheric pressure (in hPa unit) = " +str      (current_pressure) +" humidity (in percentage) = " + str(current_humidiy) + "       description = " + str(weather_description)) 

  if msg.startswith('.inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('.made'):
    quote = get_quote()
    await message.channel.send(quote)

  if msg.startswith('.help'):
    quote = get_quote()
    await message.channel.send('''
```Hello IAMDISBOT,
- .help
- .hello
- .time
- .inspire
- .lol
- .bug
- .send
- .alive
- .search
- .temp
- .spam
- .feedback ```''')
  if msg.startswith('.start'):
    quote = get_quote()
    await message.channel.send('''
```Hello IAMDISBOT,
- .help
- .hello
- .time
- .inspire
- .lol
- .bug
- .send
- .alive
- .search
- .temp
- .spam
- .feedback ```''')

  if msg.startswith('.time'):
    tt = time.strftime("%I:%M %p")
    await message.channel.send(f"its {tt}")

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith(".new"):
    encouraging_message = msg.split(".new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith(".joke"):
    sjoke = pyjokes.get_joke(language='en', category='all')
    await message.channel.send(sjoke)
  if msg.startswith(".lol"):
    sjoke = pyjokes.get_joke(language='en', category='all')
    await message.channel.send(sjoke)
  if msg.startswith(".date"):
    await message.channel.send(f"It is {date.today()}")
  if msg.startswith(".send"):
        send_message = msg.split(".send ",1)[1]
        await message.channel.send(f"{send_message}{message.author.mention}")

  if msg.startswith(".sned"):
        send_message = msg.split(".sned ",1)[1]
        await message.channel.send(f"{send_message}")

  if msg.startswith(".bug"):
    bug_message = msg.split(".bug ",1)[1]    
    def response():
      webhook.execute()
    webhook = DiscordWebhook(url='#yourwebhook', rate_limit_retry=True,
                            content=f'Issue no :- {issuegenrep};  {message.author.mention} found a Bug "{bug_message}"')
    response()
    await message.channel.send(f'''Issue no :- {issuegenrep}; 
{message.author.mention} we've reported that bug (stating '{bug_message}') we'll fix it asap''')

  if msg.startswith(".feedback"):
    bug_message = msg.split(".feedback ",1)[1]    
    def response():
      webhook.execute()
    webhook = DiscordWebhook(url='#Youe webhhook', rate_limit_retry=True,
                            content=f'Feedback by {message.author.mention} :- "{bug_message}"')
    response()
    await message.channel.send(f''' 
{message.author.mention} Thanks For the Feedback!''')


  if msg.startswith(".del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split(".del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

    if "encouragements" in db.keys():
      index = int(msg.split(".del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith(".list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith(".responding"):
    value = msg.split(".responding ",1)[1]

  if msg.startswith(".hello"):
    await message.channel.send("Hi I am a BOT i can do anything , please type .help for the list of commands.")
  if msg.startswith(".hi"):
    await message.channel.send("Hi I am a BOT i can do anything , please type .help for the list of commands.")
  if msg.startswith(".alive"):
    await message.channel.send("Hi I am a BOT i can do anything , to check if i am alive please visit 'https://Discord-Bot.brokiemag.repl.co'")

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")
  if msg.startswith(".search"):
    wiki = msg.split(".search ",1)[1]
    try:
        URL = "https://www.google.co.in/search?q=" + wiki
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        resultg = soup.find(class_='Z0LcW XcVN5d').get_text()
        await message.channel.send(resultg)
    except Exception:
                    result = wikipedia.summary(wiki, sentences=2)  
                    await message.channel.send(result)  
keep_alive()          
client.run("KEy#")