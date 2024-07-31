import folium

lon, lat = 32.881830236836265, -117.23351828641518
zoom_start = 25


m = folium.Map(location=[lon, lat], zoom_start=zoom_start)
# Define the custom tile layer
tiles = 'https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.{ext}'
attr = ('&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver '
        '(Contains Copernicus Data) | &copy; '
        '<a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> '
        '&copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> '
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors')

# Add the custom tile layer to the map
folium.TileLayer(
    tiles=tiles,
    attr=attr,
    name='Stadia Alidade Satellite',
    min_zoom=0,
    max_zoom=20,
    ext='jpg'
).add_to(m)

folium.Marker(
    location=[lon, lat],
    tooltip="Click me!",
    popup="CSE Basement",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

folium.Marker(
    location=[32.88108881238462, -117.23740766672096],
    tooltip="Click me!",
    popup="Studying Center",
    icon=folium.Icon(color="green"),
).add_to(m)


m.save("map.html")