import discord
import os
os.add_dll_directory(r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from dotenv import load_dotenv
import modelo as model


client = discord.Client()

model = model.Modelo()
sobe_modelo = model.carrega_modelo()

prefixo_bot = '$'

@client.event
async def on_ready():
  print ("O BOT TA ON")
  

@client.event
async def on_message(message):
  content = message.content.lower()
  channel = message.channel
  author = message.author.name
  attachment = message.attachments
  mention = message.author.mention


  if(author == "Pokestokyo"):
    return

  if content.startswith(prefixo_bot + "pokedex"):
      if (attachment):
         url_img = attachment[0].url_img_px
      else:
          img = content.split()
          url_img = img[1]
      response = model.previsao(sobe_modelo, url_img)
      await channel.send(response)
     

client.run("OTg0ODg3MTIwMDA1MDYyNzQ2.Ggb6hF.gMCsM9Y5xpKHBzjKzrCwUWwF1BlWtqlL8WUB8w")
