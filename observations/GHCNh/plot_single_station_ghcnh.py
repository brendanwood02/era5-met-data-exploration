import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/HEATHROW.csv')
#print(df[['Year', 'Month', 'Day', 'Hour', 'Minute', 'temperature']].head(20))

df['datetime'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour', 'Minute']]) # creates datetime column
df = df.set_index('datetime')                                                   # makes datetime the index, needed for resampling
df_t2m = df['temperature']
df_t2m_hourly = df_t2m.resample('1h').mean()
print(df_t2m_hourly)

fig, ax = plt.subplots(figsize=(12, 5))
df_t2m_hourly.plot(ax=ax)
ax.set_title(f'Heathrow 2m Temperature (°C) - First 3 days of 2025')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')

plt.savefig('heathrow_t2m.png', dpi=150, bbox_inches='tight')
print("Plot saved as heathrow_t2m.png")