# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import datetime
from datetime import timedelta
from discord import utils, Forbidden
import random
import os
from dotenv import load_dotenv
import time
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD = "jamjam's server"
bot = discord.Client(intents=discord.Intents.all())
time = timedelta(minutes=1)
global idlist
idlist = []
global endTime
endTime = datetime.datetime.now()
global cursed
cursed = dict()
global noahMuted
noahMuted = False






# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	global endTime
	global cursed
	global noahMuted
	rng = random.randint(0,100000)
	mf = False
	tomato_dm = ""
	if rng == 45829:
		await message.channel.send("RAINBOWDIVINE KILLED THE UNITED HEALTH CEO I REPEAT THAT WAS RAINBOWDIVINE WHO DID THAT THIS IS NOT A DRILL")
	if rng == 29292:
		await message.channel.send("This bot and corresponding discord group have been officially seized by the United States Department of Homeland Security. Please remain calm. Units will be dispatched shortly. This is not a drill.")
	if "!magicfind" in message.content:
		tempint = int(message.content[11:])
		mf = True
		if tempint < 100000:
			rng = random.randint(0, 100000 - tempint)
			if rng != 1:
				await message.channel.send('you rolled ' + str(rng) + ' KEEP GAMBLING')
	if rng % 10 == 0:
		tomato_dm = "ari did 9/11"
	elif rng % 7 == 0:
		tomato_dm = "I like my tomatoes drippy bruh..."
	elif rng % 5 == 0:
		tomato_dm = "meow"
	else:
		tomato_dm = "hey"
	if message.channel.id == 1130998073242427393 and (message.author.name == "Bathbot"):
		await message.delete()
	#if message.author.id == 1091869325801050193 or message.author.id == 708153981314007043 or message.author.id == 859921484122554399 or message.author.id == 633493900366970880:
		#await message.add_reaction("🍅")
	#await message.author.send("hey :3")
	if message.author.id == 733041150746820698:
		await message.delete()
	if message.author.name in cursed:
		if datetime.datetime.now() < cursed[message.author.name]:
			try:
				await message.author.send(tomato_dm)
			except Forbidden:
				await message.channel.send(message.author.name + " HAS BLOCKED TOMATO BOT WHILE CURSED! SHAME THIS USER")

	if message.author.name in cursed:
		if datetime.datetime.now() >= cursed[message.author.name]:
			del cursed[message.author.name]
	#if message.content == "me and who":
		#await message.delete()





	print(message.author.name)
	if rng == 1:
		mfstr = ""
		if mf:
			mfstr = "+ " + str(tempint) + "% Magic Find!"
		await message.channel.send("INSANE DROP: You found a Life!"  + mfstr + " Gotten by: " + message.author.name)
	if message.content == "miku":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hatsune miku did 9/11 do not trust that lying blue haired devil")
	if "meow" in message.content:
		if rng % 10 == 0:
			await message.channel.send("meow meow meow all these kids do in this generation is FUCKING meow, edate and charge they phone kamalas FUCKINg america")
		else:
			await message.channel.send("nya~ :3")
	if message.content == "hime hime":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("suki sukilling your firstborn")
	if message.content == ("!showgrade"):
		await message.channel.send("100/100 (A): 2.5% of total grade")
	if ("goon" in message.content.lower() or "g0on" in message.content.lower() or "go0n" in message.content.lower() or "g00n" in message.content.lower()) and message.author.name == "emberisuu":
		await message.author.send("no gooning")
	if message.content == "!noahsleep" and (message.author.name == "ravenaven" or message.author.name == "jamjam0"):
		noahMuted = not noahMuted
		await message.channel.send("noah mute toggled to " + str(noahMuted))
	if message.author.name == "noahsu" and noahMuted:
		if rng % 100 != 0:
			await message.delete()




@bot.event
async def on_reaction_add(reaction, user):
	print("working")
	global board
	global url
	global endTime
	global cursed
	global noahMuted
	board = reaction.message.guild.get_channel(1283226919805915219)
	if user.name == "noahsu" and noahMuted:
		await reaction.remove(user)
	if str(reaction) == "🍅":
		id2 = reaction.message.id
		if reaction.count == 3 and id2 not in idlist:
			await reaction.message.channel.send(reaction.message.author.name.upper() + " NEEDS TO SEND BETTER MESSAGES")
			url = reaction.message.jump_url
			idlist.append(reaction.message.id)
			image2 = ""
			if(reaction.message.attachments != []):
				image2 = reaction.message.attachments[0].url
			embed = discord.Embed(title = reaction.message.author.name,color=discord.Colour.blue(),url=url, timestamp=reaction.message.created_at, description=reaction.message.content)
			if(image2 != ""):
				embed.set_image(url=image2)
			await board.send(content="3🍅 | " + url, embed=embed)
			endTime = datetime.datetime.now() + datetime.timedelta(minutes=2)
			cursed[reaction.message.author.name] = endTime
			endTime = datetime.datetime.now()
			"""
			save_role = []
			roles = await reaction.message.guild.fetch_roles()
			for r in roles:
				if r.permissions.administrator:
					save_role.append(r)
					await reaction.message.author.remove_roles(r, atomic=True)
			await reaction.message.author.timeout(time)
			for r in save_role:
				await reaction.message.author.add_roles(r, atomic=True)
				"""
		elif reaction.count > 3:
			cursed[reaction.message.author.name] = cursed[reaction.message.author.name] + datetime.timedelta(minutes=1)
			if reaction.message.author.name == "ravenaven":
				cursed[reaction.message.author.name] = cursed[reaction.message.author.name] + datetime.timedelta(minutes=1)
			count = reaction.count
			message_now = await board.fetch_message(board.last_message_id)
			await message_now.edit(content=str(count) + "🍅 | " + url)
	if str(reaction) == "☢️" and reaction.count > 4:
		await reaction.message.channel.send("nuclear bomb activated on " + reaction.message.author.name)
		await reaction.message.delete()
	if str(reaction) == "⭐" and reaction.message.author.name == user.name and user.name != "Starboard#0987":
		await reaction.remove(user)
		await reaction.message.add_reaction("🍅")



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(TOKEN)