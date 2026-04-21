import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import reverse_geocoder as rg

ds = xr.open_dataset('era5_uk_precip.nc')

# print(ds)

# Select first time step
tp_6hrly = ds['tp'] * 1000
tp_daily = tp_6hrly.resample(valid_time='1D').sum()

# date_str = '2026-04-07'
# tp_daily_value = tp_daily.sel(valid_time=date_str)
day_num = 2
tp_on_day = tp_daily.isel(valid_time=day_num)

date_str = str(tp_daily['valid_time'].values[day_num])[:10]
print(f"Date: {date_str}")

# Calculate the maximum value and the location of the maximum value
max_val = tp_on_day.values.max().round(1)
max_idx = np.unravel_index(np.argmax(tp_on_day.values), tp_on_day.values.shape) # argmax finds the index of the maximum value in a flattened 1D version of the list. unravel_index then converts that flat index back into a 2D index, reflecting the array's original shape.
max_lat = tp_on_day['latitude'].values[max_idx[0]]
max_lon = tp_on_day['longitude'].values[max_idx[1]]
max_country = rg.search((max_lat, max_lon))[0]['cc']

print(f"Max precip total: {max_val}mm at {max_lat}°N, {max_lon}°E (Country: {max_country})")
print(f"Min precip total: {tp_on_day.values.min().round(1)}mm")
print(f"Mean precip total: {tp_on_day.values.mean().round(1)}mm")

fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot temperature as filled contours
tp_on_day.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='Blues', alpha=0.8)

ax.add_feature(cfeature.COASTLINE.with_scale('10m'))
ax.add_feature(cfeature.BORDERS)
ax.gridlines(draw_labels=True)

ax.set_title(f'ERA5 Daily Accumulated Rainfall (mm) - {date_str}')

plt.savefig('era5_daily_precip.png', dpi=150, bbox_inches='tight')
print("Plot saved as era5_daily_precip.png")