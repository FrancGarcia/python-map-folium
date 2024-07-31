import folium

if __name__ == "__main__":
    # create variables
    map_filepath = "folium-map.html"
    center_coord = [32.881978875195344, -117.23347001019796]
    marker_coord = [32.881978875195344, -117.23347001019796]
    marker_radius = 1_000

    # create folium map
    vmap = folium.Map(center_coord, zoom_start=15)

    # add a marker to the map
    folium.vector_layers.Circle(
        location=marker_coord,
        tooltip=f"The marker has radius {marker_radius}",
        radius=marker_radius,
        color="red",
        fill=True,
        fill_color="red"
    ).add_to(vmap)

    # store the map to a file
    vmap.save(map_filepath)