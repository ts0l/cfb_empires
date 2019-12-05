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
teams_2019 = get_team_info(year=2019)
venues = pd.read_csv('data/venues.csv')
venues = venues.rename(columns={'Unnamed: 0': 'unknown'})
venues = venues.drop(columns=['unknown', 'capacity', 'city', 'country_code', 'dome', 'elevation', 'grass', 'id', 'name', 'state', 'year_constructed', 'zip'])
venues = venues.rename(columns={'team_id': 'id'})
venues['id'] = venues['id'].apply(int)
teams_2019 = teams_2019.drop(columns=['abbreviation', 'alt_name1', 'alt_name2', 'alt_name3', 'conference', 'division', 'mascot'])
teams_venues = pd.merge(teams_2019, venues, on='id', how='outer')
teams_venues['location'] = teams_venues['location'].map(eval)
teams_venues = pd.concat([teams_venues.drop(columns=['location']), teams_venues['location'].apply(pd.Series)], axis=1)
teams_venues = teams_venues.rename(columns={'x': 'Latitude', 'y': 'Longitude'})
teams_venues.to_csv('data/teams_venues.csv', index=False)


# %%
from geopy.distance import distance

counties = pd.read_csv('data/county_loc.csv', dtype=object)
counties['FIPS'] = counties['State Code'] + counties['County Code']
counties = counties.drop(columns=['State Code', 'County Code'])

for _, row in teams_venues.iterrows():
    dist = lambda county: distance((county['Latitude'], county['Longitude']), (row['Latitude'], row['Longitude'])).km
    counties[row['school']] = counties[['Latitude', 'Longitude']].apply(dist, axis=1)

counties['Owner'] = counties[counties.columns.difference(['Name', 'Latitude', 'Longitude', 'FIPS'])].idxmin(axis=1)
counties = counties[['Name', 'FIPS', 'Owner']]
counties.to_csv('data/starting_counties.csv', index=False)

# %%
teams_venues

# %%
import pandas as pd
import plotly.figure_factory as ff

teams_venues = pd.read_csv('data/teams_venues.csv')

def empire_map(counties, name):
    teams_venues = pd.read_csv('data/teams_venues.csv')
    plotter = pd.merge(counties, teams_venues, left_on='Owner', right_on='school', how='outer')[['Name', 'FIPS', 'Owner', 'color', 'alt_color', 'logos']]
    teams_venues = teams_venues.sort_values(by='school')
    plotter = plotter.sort_values(by='Owner')
    plotter = plotter.dropna()
    fig = ff.create_choropleth(
        fips=plotter['FIPS'].tolist(), 
        values=plotter['Owner'].tolist(), 
        colorscale=teams_venues[teams_venues['school'].isin(set(plotter['Owner']))]['color'].tolist(),
        show_state_data=False, county_outline={'color': 'rgb(255,255,255)', 'width': 0.05}, title=f'Week {name}')
    fig.write_image(f'images/week{name}.png')

# %%
games = pd.read_csv('data/games.csv', encoding='latin-1')
games = games[['week', 'home_team', 'home_points', 'away_team', 'away_points']]

# %%
winner = lambda game: game['home_team'] if game['home_points'] > game['away_points'] else game['away_team']
loser = lambda game: game['home_team'] if game['home_points'] < game['away_points'] else game['away_team']
games['winner'] = games.apply(winner, axis=1)
games['loser'] = games.apply(loser, axis=1)
games = games[games['winner'].isin(teams_venues['school'])]

# %%
counties = pd.read_csv('data/starting_counties.csv')

for week in range(1, 15):
    for _, game in games[games['week'] == week].iterrows():
        counties['Owner'] = counties['Owner'].replace({game['loser']: game['winner']})
    empire_map(counties, week)
    counties.to_csv(f'data/counties_week{week}.csv', index=False)

# %%
week_14 = pd.read_csv('data/counties_week14.csv', dtype=object)
empire_map(week_14)

# %%
counties = pd.read_csv('data/starting_counties.csv')
counties

# %%
