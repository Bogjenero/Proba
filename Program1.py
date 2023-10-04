import osmnx as ox
import folium

# Postavite lokaciju na Zagreb, Hrvatska
location = "Zagreb, Croatia"

# Dobijanje grafa grada Zagreba
G = ox.graph_from_place(location, network_type="all")

# Prikaz grafa
graph_map = ox.plot_graph_folium(G, popup_attribute='name')

# Kreiranje mape i dodavanje grafa na nju
map = folium.Map(location=[45.815011, 15.981919], zoom_start=12)  # Postavite početnu lokaciju i zoom nivo po vašoj želji
graph_map.add_to(map)

# Sačuvajte mapu u HTML fajl
map.save('zagreb_map.html')