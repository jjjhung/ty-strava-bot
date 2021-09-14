import pandas as pd
import numpy as np
import json
import os
import pickle

from dotenv import load_dotenv
load_dotenv()

import strava.run_resp as strava_parser
import strava.tokens   as strava_token
import strava.call     as strava_analyt

class Stradat:

    _data_dump_file = "data.obj"

    def __init__(self):
        
        self._users = json.loads(os.environ['STRAVA_USERS_ALL'])
        self.read_data()

        if self._data.empty:
            self._data = pd.DataFrame()

        self.set_database()

    def get_leaderboard(self,timeframe:str = "week") -> str:
        '''
        Returns total activity leaderboard for specified timeframe (default weekly)
        
        parameters
        ===============
        timeframe: ['week','month','year']

        returns
        =============
        Print-ready formatted string
        '''


    def get_recent_activities(self, start: pd.Timestamp = None, end:pd.Timestamp = None) -> str:
        '''
        Returns recent acvitites within specified timeframe (default one hour)
        
        parameters
        ===============
        start       pandas timestamp start activity retrieval time
        end         pandas timestamp end activity retrieval time

        returns
        =============
        Print-ready formatted string
        '''

        all_new_ath_activities = pd.DataFrame()
        for user in self._users:
            print("Retrieving %s" %(user))
            access_token = strava_token.read_access_token(user)
            new_ath_activities = strava_analyt.act_api(access_token)
            all_new_ath_activities = all_new_ath_activities.append(new_ath_activities, ignore_index=True)


        self._data = self._data.append(all_new_ath_activities, ignore_index=True)
        self._data.drop_duplicates(subset=['Activity ID'], inplace=True, ignore_index=True,keep="first")
        self.dump_data()

        print(self._data)
        return all_new_ath_activities



    def read_data(self):
        file_handler = open('../pickled/%s'%(self._data_dump_file),'rb')
        self._data = pickle.load(file_handler)

    def dump_data(self):
        file_handler = open('../pickled/%s'%(self._data_dump_file),'wb')
        pickle.dump(self._data, file_handler)


    def set_database(self):
        '''Build database
        '''


        for user in self._users:
            print("Retrieving %s"%(user))
            strava_tierup_access = strava_token.read_access_token(user)

            ath_activities = strava_analyt.act_api(strava_tierup_access)
            self._data = self._data.append(ath_activities, ignore_index=True)

        self.dump_data()


    def get_unposted_activities(self) -> str:
        if self._data.loc[self._data['Posted'] == False].empty:
            return ''
        else:
            return self.strify(self._data.loc[self._data['Posted'] == False])


    def get_printable_activities_all(self):
        '''Get a string representation of all activities
        '''
        return '' if self._data.empty else self.strify(self._data)


    def set_posted_all(self) -> None:
        '''
        Mark all data as having been posted
        '''

        self._data['Posted'] = True
        self.dump_data()

    def strify(self, df):
        '''
        Return string representation of activity details
        '''
        #print(list(df.columns))
        strfactivity = ">>> \n**{Name}**\n**Activity**: __{Activity Name}__\n**Time**: {Start Time}\n**Type**: {Type}\n**Distance**: {Distance} km\n**Moving Time**: {Moving Time}\n\
**Elapsed Time**: {Elapsed Time}\n**Elevation**: {Elevation Gain} m\n**Average Speed**: {Average Speed} km/h".format
        
        # And format
        #cols_to_keep = ['Name', 'Activity Name','Start Time','Type','Distance','Moving Time','Elapsed Time','Elevation Gain','Average Speed']
        return df.apply(lambda x: strfactivity(**x), 1)
