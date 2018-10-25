#Pyton 3.7

"""
Basic Discord bot by REV 
Will display current map on source servers as 'now playing'

"""

import discord
import valve.source.a2s
import asyncio

client = discord.Client()

async def get_map():
	while True:
		try:
			while True: #60 Second loop to query target server
				with valve.source.a2s.ServerQuerier(('<server ip>', <server port>)) as server: #IP & port must be in a tuple 
					c_map = server.info()['map']
					await client.change_presence(game=discord.Game(name=c_map))
					await asyncio.sleep(10)
		except valve.source.NoResponseError: #Server time out handler. Will print to console and desired discord channel if wanted
			await client.send_message(discord.Object(id='<discord channel id>'),'Server timed out') #discord.Object id is channel id
			print('Server timed out')
			await asyncio.sleep(20)
			server.close()



@client.event
async def on_ready(): 
	print('Logging in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
	try: #do this to run the get_map() routine.
		asyncio.ensure_future(get_map())
		
	except KeyboardInterrupt:
		pass



TOKEN = 'Secret Bot Token'
client.run(TOKEN)
