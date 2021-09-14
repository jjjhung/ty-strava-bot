import pandas as pd
import datetime

def parse_api_response_athlete_activity(responses:list, athlete:dict) -> pd.DataFrame:
    ''' Parse strava athlete api response for recent activities
        
        parameters
        ===========
        responses: list of activities 
        athlete: strava athlete details

        returns
        ===========
            Returns string representation of response with specified labels kept
                    pandas DataFrame of filtered data
    '''
    col_to_keep = [
            "name",
            "start_date_local",
            "type",
            "distance",
            "moving_time",
            "elapsed_time",
            "total_elevation_gain",
            "average_speed",
            "athlete",
            "id"
        ]

    renamed_cols = ["Activity Name",
                    "Start Time",
                    "Type",
                    "Distance",
                    "Moving Time",
                    "Elapsed Time",
                    "Elevation Gain",
                    "Average Speed",
                    "Athlete",
                    "Activity ID",
                    "Posted"
                    ]
    activities = pd.DataFrame(columns = renamed_cols)

    for i,single_response in enumerate(responses):
        new_dict = {renamed_cols[j]: [getattr(single_response,k)] for j,k in enumerate(col_to_keep)}
        new_df = pd.DataFrame(new_dict)

        activities = activities.append(new_df,ignore_index=True)

    activities['Posted'] = False
    # Convert Units and round to two decimals
    activities['Distance'] = round(activities['Distance'] / 1000, 2)
    #if activities['Type'] == "Run":
    #    activities['Average Speed'] = round(activities['Average Speed'] * 3.6,2) #Change
    #elif activities['Type'] == "Ride":
    activities['Average Speed'] = round(activities['Average Speed'] * 3.6,2)

    activities['Moving Time'] = activities['Moving Time'].apply(lambda x: str(datetime.timedelta(seconds=x)))
    activities['Elapsed Time'] = activities['Elapsed Time'].apply(lambda x: str(datetime.timedelta(seconds=x)))

    # And set athlete name
    #print(getattr(athlete,'firstname'))
    activities.insert(0, 'Name', "%s %s"%(getattr(athlete,'firstname'), getattr(athlete,'lastname')))
    return activities 


#def retrieve_athlete_name(responses:list) -> str:

