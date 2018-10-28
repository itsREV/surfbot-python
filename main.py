#Python 3.6+

"""
Discord Bot by REV

"""
import discord
import valve.source.a2s
import asyncio
from discord.ext import commands
import os
#import aiomysql

bot = commands.Bot(command_prefix='!')

"""with open('config.json') as f:
    file_dict = json.load(f)
    token = file_dict['token']
    prefix = file_dict['prefix']
    dbhost = file_dict['dbhost']
    dbuser = file_dict['dbuser']
    dbpass = file_dict['dbpass']
    dbname = file_dict['dbname']  
		dbport = file_dict['dbport'] """


async def display_map():
	while True:
		try:
			while True: #60 Second loop to query target server
				with valve.source.a2s.ServerQuerier(('136.63.63.121', 27015)) as server: #IP & port must be in a tuple 
					c_map = server.info()['map']
					await bot.change_presence(game=discord.Game(name=c_map))
					await asyncio.sleep(10)
		except valve.source.NoResponseError: #Server time out handler. Will print to console and desired discord channel if wanted
			#await client.send_message(discord.Object(id='<discord channel id>'),'Server timed out') #discord.Object id is channel id
			print('Server timed out')
			await asyncio.sleep(20)
			server.close()

@bot.command()
async def online():
	with valve.source.a2s.ServerQuerier(('136.63.63.121', 27015)) as server:
		players = server.info()['player_count']
		await bot.say(f"There are currently {players} people surfing")


@bot.event
async def on_ready():
	print("Bot has come online")
	asyncio.ensure_future(display_map())
"""
fuck mysql
@bot.command()
async def mtop(ctx, surfmap):
	
	#display top 10 times of surfmap

	
	conn = await aiomysql.connect(host=dbhost, port=dbport, user=dbuser, password=dbpass, db=dbname, loop=loop)
	async with conn.cursor() as cur:
        await cur.execute("SELECT name, MIN(runtimepro) FROM CAKEDB WHERE mapname = %s AND runtimepro > -1.0 AND style = 0", (surfmap))
				result = await cur.fetchall()
				for data in result:
					map
"""

token = os.environ.get("secret")
bot.run(token)