#Python 3.6+

"""
Surf-Bot by REV
'!online' to display current player count of server
Also displays current map as now playing
"""

import discord
import valve.source.a2s
import asyncio
import json
from discord.ext import commands


bot = commands.Bot(command_prefix=('!'))

with open('config.json') as config:  #settings yo
	file_dict = json.load(config)
	token = file_dict['token']
	ip = file_dict['ip']


async def display_map():
	while True:
		try:
			while True: #60 Second loop to query target server
				with valve.source.a2s.ServerQuerier(('136.63.63.121', 27015)) as server: #IP & port must be in a tuple 
					c_map = server.info()['map']
					await bot.change_presence(game=discord.Game(name=c_map))
					await asyncio.sleep(10)
		except valve.source.NoResponseError: #Server time out handler. Will print to console and desired discord channel if wanted
			#await bot.say(discord.Object(id='<discord channel id>'),'Server timed out') #discord.Object id is channel id
			print('Server timed out')
			await asyncio.sleep(20)
			server.close()

@bot.command()
async def online():
	"""
	Displays current player count to channel

	"""
	with valve.source.a2s.ServerQuerier((ip, 27015)) as server:
		players = server.info()['player_count']
		if players == 0:
			await bot.say("Nobody is surfing currently :(")
		elif players == 1:
			await bot.say("There is currently one person surfing!")
		else:
			await bot.say(f"There are currently {players} people surfing!")


@bot.event
async def on_ready(): 
	print('Logging in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	
	try: 
		asyncio.ensure_future(display_map())
		
	except KeyboardInterrupt:
		pass



bot.run(token)