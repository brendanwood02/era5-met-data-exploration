import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['total_precipitation'],
        'year': '2026',
        'month': '04',
        'day': ['07', '08', '09', '10', '11', '12', '13'],
        'time': ['00:00', '06:00', '12:00', '18:00'],
        'area': [72, -25, 34, 45],  # North, West, South, East boundaries of box (lat_max, lon_min, lat_min, lon_max). UK = [60, -10, 50, 2], EU = [72, -25, 34, 45]
        'format': 'netcdf',
    },
    'era5_uk_precip.nc'
)

print("Download complete!")