import pandas as pd

stations_selected = {
    'ST JAMES PARK': 'UKM00003770',
    'ANDREWSFIELD':  'UKM00003684',
    'TOPCLIFFE':     'UKI0000EGXZ',
    'ALTNAHARRA':    'UKM00003044',
    'MANCHESTER':    'UKI0000EGCC',
    'EXETER':        'UKI0000EGTE',
    'HEATHROW':      'UKI0000EGLL'
}

start_date = '2025-01-01'
end_date = '2025-01-03'

for name, ghcn_id in stations_selected.items():
    url = f"https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-historical-climatology-network-hourly&stations={ghcn_id}&startDate={start_date}&endDate={end_date}&format=csv"
    print(url)
    df = pd.read_csv(url)
    filename = f"data/{name.replace(' ', '_')}.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename} — {len(df)} rows")