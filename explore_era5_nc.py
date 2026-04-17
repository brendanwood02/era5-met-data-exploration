import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

ds = xr.open_dataset('era5_uk_temp.nc')

# First time step, converted to Celsius
t2m = ds['t2m'].isel(valid_time=0) - 273.15
time_str = str(ds['valid_time'].values[0])[:16]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': ccrs.PlateCarree()})

t2m.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu_r', label='°C')

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)
ax.gridlines(draw_labels=True)

ax.set_title(f'ERA5 2m Temperature (°C) — {time_str}')

plt.savefig('era5_temp.png', dpi=150, bbox_inches='tight')
print("Plot saved as era5_temp.png")