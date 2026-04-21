import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['2m_temperature'],
        'year': '2024',
        'month': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        'day': [f'{d:02d}' for d in range(1, 32)],
        'time': ['12:00'],
        'area': [60, -10, 50, 2],  # North, West, South, East boundaries of box (lat_max, lon_min, lat_min, lon_max) - roughly UK
        'format': 'netcdf',
    },
    'era5_uk_temp_2024.nc'
)

print("Download complete!")