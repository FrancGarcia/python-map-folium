'''
Source code and examples found here: https://github.com/basvdl97/python-folium/blob/main/%234%20-%20Adding%20onClick%20Interactions/main.py
'''


import folium


def find_popup_slice(html):
    '''
    Find the starting and ending index of the popup function
    '''

    pattern = "function latLngPop(e)"

    starting_index = html.find(pattern)

    tmp_html = html[starting_index:]

    found = 0
    index = 0
    opening_found = False
    while not opening_found or found > 0:
        if tmp_html[index] == "{":
            found += 1
            opening_found = True
        elif tmp_html[index] == "}":
            found -= 1

        index += 1

    # Find the ending index of the popup function
    ending_index = starting_index + index

    return starting_index, ending_index



def find_variable_name(html, name_start):
    variable_pattern = "var "
    pattern = variable_pattern + name_start

    starting_index = html.find(pattern) + len(variable_pattern)
    tmp_html = html[starting_index:]
    ending_index = tmp_html.find(" =") + starting_index

    return html[starting_index:ending_index]



def custom_code(popup_variable_name, map_variable_name):
    return '''
            // Adding functionality to allow to add new markers in real time
            function latLngPop(e) {
                //%s
                //    .setLatLng(e.latlng)
                //    .setContent("Latitude: " + e.latlng.lat.toFixed(4) +
                //                "<br>Longitude: " + e.latlng.lng.toFixed(4))
                //    .openOn(%s);

                //console.log("Latitude: " + e.latlng.lat.toFixed(4));
                //console.log("Longitude: " + e.latlng.lng.toFixed(4));

                var description = prompt("Enter a description for this marker:");

                var circle = L.circle(
                    [e.latlng.lat, e.latlng.lng],
                    {"bubblingMouseEvents": true, "color": "red", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "red", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0,"radius": 5, "stroke": true, "weight": 3}
                ).addTo(%s);

                if (description) {
                    circle.bindPopup(description);
                }
            }
            // End custom code
    ''' % (popup_variable_name, map_variable_name, map_variable_name)

if __name__ == "__main__":
    map_filepath = "folium-map.html"
    center_coords = [32.88195184526258, -117.23350219670715]

    map = folium.Map(center_coords, zoom_start=20)

    # Add popup
    folium.LatLngPopup().add_to(map)

    # Store the map to a file
    map.save(map_filepath)

    # Read the folium file
    html = None
    with open(map_filepath, 'r') as mapfile:
        html = mapfile.read()

    # Find variable names
    map_variable_name = find_variable_name(html, "map_")
    popup_variable_name = find_variable_name(html, "lat_lng_popup_")

    # Determine popup function indicies
    pstart, pend = find_popup_slice(html)

    # Inject custom JavaScript code to allow to add markers on the map in real time
    with open(map_filepath, 'w') as mapfile:
        mapfile.write(
            html[:pstart] + \
            custom_code(popup_variable_name, map_variable_name) + \
            html[pend:]
        )
    

    