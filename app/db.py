import pandas as pd
from geopy.geocoders.base import GeocoderTimedOut

from config import geolocator


class County:
    def __init__(self, name, county_code, state_code):
        self.name = name
        self.county_code = county_code
        self.state_code = state_code


    def lookup(self):
        query = {'county': name,
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


    def generate_states_dict(filename):
        states = pd.read_csv(filename,
                            dtype=object).set_index('State Code')['Name'].to_dict()


    def generate_counties_df(filename):
        counties = pd.read_csv('data/county_fips.csv', dtype=object)
        counties.loc[counties['State Code'] == '72',
                    'Name'] = ''  # allows lookup of Puerto Rico
        return counties


    def write_counties(counties, destination):
        counties.to_csv(destination, index=False)


    def create_county_loc():
        generate_states_dict('data/state_fips.csv')
        counties = generate_counties_df('data/')
        counties['Latitude'], counties['Longitude'] = zip(
            *counties.apply(lookup, axis=1))
