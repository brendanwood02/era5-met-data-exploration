import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': ['2m_temperature', '10m_u_component_of_wind', '10m_v_component_of_wind'],
        'year': '2026',
        'month': '04',
        'day': ['01', '02', '03'],
        'time': ['00:00', '06:00', '12:00', '18:00'],
        'area': [60, -10, 50, 2],  # North, West, South, East - roughly UK
        'format': 'netcdf',
    },
    'era5_uk_temp_wind.nc'
)

print("Download complete!")