import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import PIL.Image
import os

ds = xr.open_dataset('era5_uk_temp_wind.nc')

lats = ds['latitude'].values
lons = ds['longitude'].values
thin = 3
lons_thin = lons[::thin]
lats_thin = lats[::thin]

frames = []

for i in range(len(ds['valid_time'])):
    t2m = ds['t2m'].isel(valid_time=i) - 273.15
    u10 = ds['u10'].isel(valid_time=i)
    v10 = ds['v10'].isel(valid_time=i)
    time_str = str(ds['valid_time'].values[i])[:16]

    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})

    t2m.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu_r', alpha=0.8,
             vmin=ds['t2m'].values.min() - 273.15,
             vmax=ds['t2m'].values.max() - 273.15)

    u_thin = u10.values[::thin, ::thin]
    v_thin = v10.values[::thin, ::thin]
    ax.quiver(lons_thin, lats_thin, u_thin, v_thin,
              transform=ccrs.PlateCarree(),
              scale=150, color='black', alpha=0.7)

    ax.add_feature(cfeature.COASTLINE.with_scale('10m'))
    ax.add_feature(cfeature.BORDERS)
    ax.gridlines(draw_labels=True)
    ax.set_title(f'ERA5 2m Temperature (°C) and 10m Wind - {time_str}')

    # Save frame to file
    frame_path = f'frame_{i:02d}.png'
    plt.savefig(frame_path, dpi=100, bbox_inches='tight')
    plt.close()
    frames.append(frame_path)
    print(f"Frame {i+1}/{len(ds['valid_time'])} done")

# Stitch frames into GIF
images = [PIL.Image.open(f) for f in frames]
images[0].save('era5_animation.gif',
               save_all=True,
               append_images=images[1:],
               duration=1000,
               loop=0) # loop=0 means infinite loop

# Clean up frame files
for f in frames:
    os.remove(f)

print("Animation saved as era5_animation.gif")