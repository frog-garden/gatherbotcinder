import asyncio
import discord
import random

from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready to use!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("/gather"):
        await client.send_message(message.channel, random.choice([ "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",
                                                                   "```yaml\n --------------------------------\n What the...? A ||Perfectly Rounded Pebble|| rests at your paws. (1 point)\n --------------------------------```",]))

client.run("NTQzNTYyNjczMDMyMjY1NzQz.Dz-2Tg.odSGxfaDJMjBkpVY7C86cNdwEx0")
client.login(process.env.BOT_TOKEN);
