import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from mcpe_query.query import Query

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') 


bot = commands.Bot(command_prefix='!')

@bot.command()
async def status(ctx, ):
  host = 'drockhcf.ddns.net'
  port = 19101 #yourport 
  q = Query(host, port)
  data = q.query()
  online = data.num_players
  max = data.max_players
  jugadores = str(data.players)
  
  embed = discord.Embed(title="Survival", description=f"IP: {host} PUERTO:, {port}",color=discord.Color.random())
  
  embed.add_field(name="HCF:", value=f"ACTIVOS: {online} de {max} \n \n JUGADORES: {jugadores}", inline=False)
  
  embed.add_field(name="invita a tus amigos",  value='[TOCA AQUI PARA INVITAR (https://discord.gg/JdWFHx8pvE)')
  
  embed.set_footer(text=f" juega y diviertete!! ")
  
  await ctx.send(embed=embed)
  print(jugadores)
  
  @bot.command()
  async def uwu(ctx):
  	await ctx.send('UwUr')

@bot.command()

@commands.has_permissions(administrator=True)
async def say(ctx,*,text):
	await ctx.message.delete()
	await ctx.send(text)




bot.run(TOKEN)
