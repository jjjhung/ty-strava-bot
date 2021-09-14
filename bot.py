import os

import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
load_dotenv()

import time
import pprint 
import swagger_client


import strava.run_resp as strava_parser
import strava.tokens   as strava_token
import strava.call     as strava_analyt
import data


def launch():
    
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    DISCORD_GUILD = os.getenv('DISCORD_GUILD')
    DISCORD_BOT_CHANNEL_ID = os.getenv('DISCORD_BOT_CHANNEL_ID')

    #client = discord.Client()
    client = commands.Bot(command_prefix = '~')
    channel = client.get_channel(int(DISCORD_BOT_CHANNEL_ID))

    all_data = data.Stradat()


    # ~strava command to test individuals
    @client.command()
    async def strava(context):
        #strava_tierup_access = tokens.read_access_token("TANK")

        #response = analyt.act_api(strava_tierup_access)
        activities = all_data.get_printable_activities_all()

        for res in activities:
            await context.send(res)



    # Hourly activities update
    @tasks.loop(minutes=1)
    async def retr_new_activities():

        recent = all_data.get_recent_activities()
        channel = client.get_channel(int(DISCORD_BOT_CHANNEL_ID))

        #activities = all_data.get_printable_activities_short(recent)
        activities = all_data.get_unposted_activities()
        all_data.set_posted_all()

        for res in activities:
            await channel.send(res)



    # Initialization tasks
    @client.event
    async def on_ready(): # Connected to discord
        for guild in client.guilds:
            if guild.name == DISCORD_GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        retr_new_activities.start()


    client.run(DISCORD_TOKEN)

def test():
    strava_tierup_access = strava_token.read_access_token("JOSEPH")
    #all_data = data.Stradat()
    print(strava_analyt.act_api(strava_tierup_access))
    #analyt.ath_api(strava_tierup_access)
    #analyt.club_api(strava_tierup_access)
    #print(strava_analyt.act_api(strava_tierup_access)['Type'])
    
    #all_data = data.Stradat()


if __name__ == '__main__':
    #test()
    launch()