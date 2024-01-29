import discord
import os
import time
from LCG_random import *


token = "MTIwMTIwMzQ3ODgxOTc3NDYyNQ.GGnorO.pD6ndCODxoHEivYa-LQjjABiNxosEYlsU0LKHM"


client = discord.Client(intents=discord.Intents.all())

number = LCG()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"$int_uniform"):
        string = str(message.content)
        i = string.find("[")
        j = string.find(",")
        k = string.find("]")

        a = ""
        b = ""

        for char in range(i+1 , j):
            a += string[char]
        a = int(a)
        for char in range(j+1 , k):
            b+= string[char]
        b = int(b)
        await message.channel.send(number.int_generator([a,b]))

    if message.content.startswith("$deci_uniform"):
        string = str(message.content)
        i = string.find("[")
        j = string.find(",")
        k = string.find("]")

        a = ""
        b = ""

        for char in range(i+1 , j):
            a += string[char]
        a = int(a)
        for char in range(j+1 , k):
            b+= string[char]
        b = int(b)
        await message.channel.send(number.float_generator([a,b]))

    if message.content.startswith("$deci_uniform"):
        string = str(message.content)
        i = string.find("[")
        j = string.find(",")
        k = string.find("]")

        mean = ""
        variance = ""

        for char in range(i+1 , j):
            mean += string[char]
        mean = int(a)
        for char in range(j+1 , k):
            variance += string[char]
        variance = int(b)
        await message.channel.send(number.normal_genarator(mean=mean, variance=variance))

client.run(token)