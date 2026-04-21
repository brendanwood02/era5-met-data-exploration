import xarray as xr

ds = xr.open_dataset('era5_uk_temp.grib', engine='cfgrib')

t2m_celsius = ds['t2m'].isel(time=0) - 273.15
print("Min temp (C):", t2m_celsius.values.min().round(1))
print("Max temp (C):", t2m_celsius.values.max().round(1))
print("Mean temp (C):", t2m_celsius.values.mean().round(1))