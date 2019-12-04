import pandas as pd
from geopy.geocoders.base import GeocoderTimedOut

from config import geolocator, states_fips, county_fips, county_locs


class County:
    states = generate_states_dict(states_fips)

    def __init__(self, name, county_code, state_code):
        self.name = name
        self.county_code = county_code
        self.state_code = state_code
        self.latitude = 0
        self.longitude = 0

    def lookup(self, states):
        query = {'county': self.name,
                 'state': states[self.state_code]}
        try:
            obj = geolocator.geocode(query)
            self.latitude = obj.latitude
            self.longitude = obj.longitude
        except AttributeError:
            print(
                f"-------------------------\n{self.name}, {states[self.state_code]} not found.")
        except GeocoderTimedOut:
            print(
                f"-------------------------\nHERE timed out. on {self.name}, {states[self.state_code]}")


def generate_states_dict(filename):
    return pd.read_csv(filename,
                       dtype=object).set_index('State Code')['Name'].to_dict()


def generate_counties_list(filename):
    counties = pd.read_csv(filename, dtype=object)
    counties.loc[counties['State Code'] == '72',
                 'Name'] = ''  # allows lookup of Puerto Rico
    return counties

"""
Deprecated from tests, will need to rewrite for production.
"""
# def write_counties(counties, destination):
#     counties.to_csv(destination, index=False)


# def create_county_loc():
#     generate_states_dict(states_fips)
#     counties = generate_counties_df(county_fips)
#     counties['Latitude'], counties['Longitude'] = zip(
#         *counties.apply(lookup, axis=1))
#     write_counties(counties, county_locs)
