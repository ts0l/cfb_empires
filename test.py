# %%
import pandas as pd
from geopy.geocoders.base import GeocoderTimedOut
from geopy.geocoders import Here

geolocator = Here('kO1cowFWMjjOgIKv6cFd', '_llArvZJD-XXKWs4q41hkQ')

# %%
states = pd.read_csv('data/state_fips.csv',
                     dtype=object).set_index('State Code')['Name'].to_dict()
counties = pd.read_csv('data/county_fips.csv', dtype=object)
counties.loc[counties['State Code']=='72', 'Name'] = ''


# %%
def lookup(county):
    query = {'county': county['Name'],
             'state': states[county['State Code']]}
    lat, lon = 0, 0
    try:
        obj = geolocator.geocode(query)
        lat, lon = obj.latitude, obj.longitude
    except AttributeError:
        print(
            f"-------------------------\n{county['Name']}, {states[county['State Code']]} not found.")
    except GeocoderTimedOut:
        print(
            f"-------------------------\nHERE timed out. on {county['Name']}, {states[county['State Code']]}")
    finally:
        return lat, lon

#%%
counties['Latitude'], counties['Longitude'] = zip(*counties.apply(lookup, axis=1))
counties.to_csv('data/county_loc.csv', index=False)

#%%
import CFBScrapy as cfb

teams = cfb.get_team_info()
teams

# %%
venues = cfb.get_venue_info()
venues

# %%
teams.to_csv('data/teams.csv')

# %%
import requests

def get_team_info(year, conference=None):
    '''
        Returns a DataFrame containing color, logo, and mascot info
        about each team in the queried params
        conference (optional) = queries by conference
    '''
    base_url = 'https://api.collegefootballdata.com/teams/fbs'
    payload = {}

    if conference is not None:
        payload['conference'] = conference
    payload['year'] = year
    
    r = requests.get(base_url, params=payload)
    if r.status_code == 200:
        return pd.DataFrame(r.json())
    else:
        raise Exception('Request failed with status code: '+str(r.status_code))

teams_2019 = get_team_info(year=2019)
teams_2019

# %%
teams_2019.to_csv('data/teams_2019.csv')

# %%
venues = pd.read_csv('data/venues.csv')
venues

# %%
