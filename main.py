import discord
import os
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from dotenv import load_dotenv
import modelo as model



model = model.Model()
loaded_model = model.load_model()


client = discord.Client()

prefix = '$'

@client.event
async def on_ready():
  print ("O BOT TA ON")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=prefix+"help"))

@client.event
async def on_message(message):
  content = message.content.lower()
  channel = message.channel
  author = message.author.name
  anexo = message.attachments
  mention = message.author.mention

  if(author == "Pokestokyo"):
    return


  if content.startswith(prefix + "pokedex"):
      if (anexo):
         url = anexo[0].proxy_url
      else:
          img = content.split()
          url = img[1]
      response = model.predict(loaded_model, url)
      await channel.send(response)
     


client.run("OTg0ODg3MTIwMDA1MDYyNzQ2.Ggb6hF.gMCsM9Y5xpKHBzjKzrCwUWwF1BlWtqlL8WUB8w")
