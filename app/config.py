from geopy.geocoders import Here

HERE_app_id = 'kO1cowFWMjjOgIKv6cFd'
HERE_app_code = '_llArvZJD-XXKWs4q41hkQ'

geolocator = Here(HERE_app_id, HERE_app_code)

states_fips = '../data/state_fips.csv'
county_fips = '../data/county_fips.csv'
county_locs = '../data/county_loc.csv'
