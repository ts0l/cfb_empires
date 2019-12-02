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
