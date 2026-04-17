import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

ds = xr.open_dataset('era5_uk_temp_wind.nc')

print(ds)

# Select first time step
t2m = ds['t2m'].isel(valid_time=0) - 273.15
u10 = ds['u10'].isel(valid_time=0)
v10 = ds['v10'].isel(valid_time=0)
time_str = str(ds['valid_time'].values[0])[:16]

# Get coordinate arrays
lats = ds['latitude'].values
lons = ds['longitude'].values

# Thin the wind arrows - every 3rd point so they don't overlap
thin = 3
lons_thin = lons[::thin]
lats_thin = lats[::thin]
u_thin = u10.values[::thin, ::thin]
v_thin = v10.values[::thin, ::thin]

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

# Plot temperature as filled contours
t2m.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu_r', alpha=0.8)

# Plot wind arrows on top
ax.quiver(lons_thin, lats_thin, u_thin, v_thin,
          transform=ccrs.PlateCarree(),
          scale=150, color='black', alpha=0.7)

ax.add_feature(cfeature.COASTLINE.with_scale('10m'))
ax.add_feature(cfeature.BORDERS)
ax.gridlines(draw_labels=True)

ax.set_title(f'ERA5 2m Temperature (°C) and 10m Wind - {time_str}')

plt.savefig('era5_temp_wind.png', dpi=150, bbox_inches='tight')
print("Plot saved as era5_temp_wind.png")