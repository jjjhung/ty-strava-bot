import requests
import json
import os
import time
from dotenv import load_dotenv
load_dotenv()


def get_access_token(name:str) -> str:
    '''
    Get access token for athlete. Must have provided auth code, which is stored in env variable.
    Only need to perform this once per athlete. 
    
    If this is run again, a new code must be generated with the strava oauth request::

    https://www.strava.com/oauth/authorize?client_id=69663&response_type=code&
        redirect_uri=http://localhost/exchange_token&approval_prompt=force&
        scope=read,read_all,profile:read_all,activity:read,activity:read_all

    '''
    response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                                'client_id': int(os.getenv('STRAVA_CLIENT_ID')),
                                'client_secret': os.getenv('STRAVA_CLIENT_SECRET'),
                                'code': os.getenv('STRAVA_CODE_%s'%(name)),
                                'grant_type': 'authorization_code'
                                }
                    )
    strava_tokens = response.json()
    print(strava_tokens)
    with open('strava_tokens_%s.json'%(name), 'w') as outfile:
        json.dump(strava_tokens, outfile)

    with open('strava_tokens_%s.json'%(name)) as fs:
        strava_tokens = json.load(fs)

    return strava_tokens['access_token']

def read_access_token(name:str) -> str:
    '''
    Read access token for athlete, stored in json file. 
    If access token is expired, a refresh request is submitted. 
    '''

    with open('strava_tokens_%s.json'%(name)) as fs:
      strava_tokens = json.load(fs)

    # Check refresh
    if strava_tokens['expires_at'] < time.time():
        response = requests.post(
            url = 'https://www.strava.com/oauth/token',
            data = {
                    'client_id': int(os.getenv('STRAVA_CLIENT_ID')),
                    'client_secret': os.getenv('STRAVA_CLIENT_SECRET'),
                    'grant_type': 'refresh_token',
                    'refresh_token': strava_tokens['refresh_token']
                    }
        )
        new_strava_tokens = response.json()


        with open('strava_tokens_%s.json'%(name), 'w') as fs:
            json.dump(new_strava_tokens, fs)

        strava_tokens = new_strava_tokens
    
    return strava_tokens['access_token']
