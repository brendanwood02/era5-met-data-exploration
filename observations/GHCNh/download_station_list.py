## Use this script to obtain the ghcnh_ids of sites you wish to get data for

import pandas as pd

pd.set_option('display.max_rows', None)

url = 'https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/doc/ghcnh-station-list.csv'
stations = pd.read_csv(url)
uk_stations = stations[stations['ISO_CODE'] == 'GB']
#uk_active = uk_stations[uk_stations['ICAO'].notna()]

print(uk_stations)
print(len(uk_stations))
#print(uk_stations['STATION NAME'])