from dotenv import load_dotenv
load_dotenv()

import os
import swagger_client
import requests
import pandas
import time
from pandas.io.json import json_normalize
import json

import strava.run_resp as strava_parser

STRAVA_TOKEN  = os.getenv('STRAVA_ACCESS')
STRAVA_REFRESH  = os.getenv('STRAVA_REFRESH')

STRAVA_RUN_ID  = os.getenv('STRAVA_RUN_ID')
#STRAVA_CYCLE_ID = os.getenv("STRAVA_BIKE_ID") Not Yet


def ath_api(token):
	strava_inst = swagger_client.AthletesApi()
	strava_inst.api_client.configuration.access_token = token

	api_response = strava_inst.get_logged_in_athlete()
	return api_response


def club_api(token):
	strava_inst = swagger_client.ClubsApi()
	strava_inst.api_client.configuration.access_token = token #STRAVA_TOKEN
	api_response = strava_inst.get_club_members_by_id(STRAVA_RUN_ID, per_page=5)
	return

def act_api(token):
	'''
	List most recent athlete activities in past 1 hour period

	Returns dataframe of activities
	'''	
	strava_inst = swagger_client.ActivitiesApi()
	strava_inst.api_client.configuration.access_token = token#STRAVA_TOKEN

	#api_response = strava_inst.get_activity_by_id(id=5844978168, include_all_efforts=False)
	curr_time = int(time.time())
	print(curr_time)
	api_response_activity = strava_inst.get_logged_in_athlete_activities()#after=curr_time-40000)
	api_response_athlete = ath_api(token)

	#print(api_response)
	return strava_parser.parse_api_response_athlete_activity(api_response_activity, api_response_athlete)
