import pandas as pd
import matplotlib.pyplot as plt

stations_selected = {
    'ST JAMES PARK': 'UKM00003770',
    'ANDREWSFIELD':  'UKM00003684',
    'TOPCLIFFE':     'UKI0000EGXZ',
    'ALTNAHARRA':    'UKM00003044',
    'MANCHESTER':    'UKI0000EGCC',
    'EXETER':        'UKI0000EGTE',
    'HEATHROW':      'UKI0000EGLL'
}

fig, ax = plt.subplots(figsize=(12, 5))
ax.set_title('2m Temp Across Various Locations — First 3 Days of 2025')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')

for name in stations_selected:
    filename = f"data/{name.replace(' ', '_')}.csv"
    df = pd.read_csv(filename)
    df['datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']])
    df = df.set_index('datetime')
    df_t2m_hourly = df['temperature'].resample('1h').mean()
    df_t2m_hourly.plot(ax=ax, label=name)

ax.legend()
plt.savefig('compare_t2m.png', dpi=150, bbox_inches='tight')
print("Plot saved as compare_t2m.png")