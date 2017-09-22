import plotly as py                                     #import lib plotly
import pandas as pd                                     #import lib pandas

df_airports = pd.read_csv('airport.csv')                #mengambil data airport
df_airports.head()

df_flight_paths = pd.read_csv('flight_paths.csv')       #mengambil data jalur penerbangan
df_flight_paths.head()

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

airports = [ dict(                                      #pendataan airport
        type = 'scattergeo',                            #type yang digunakan untuk data geografis
        locationmode='USA-states',
        lon = df_airports['long'],                      #mengambil longitude dari data
        lat = df_airports['lat'],                       #mengambil latitude dari data
        hoverinfo = 'text',                             #informasi di hover
        text = df_airports['airport'],                  #isi informasi hover dengan nama airport
        mode = 'markers',                               #mode untuk menampilkan marker di titik
        marker = dict(                                  #membuat bentuk marker
            size=5,                                     #ukuran marker
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',                          #bentuk marker
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = df_airports['cnt'],
            cmax = df_airports['cnt'].max(),
        ))]
        
flight_paths = []                                       #membuat jalur penerbangan
for i in range( len( df_flight_paths ) ):
    flight_paths.append(
        dict(
            type = 'scattergeo',                                                        #type yang digunakan untuk data geografis
            lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],   #mengambil longitude dari data
            lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],   #mengambil latitude dari data
            mode = 'lines',                                                             #membuat garis
            line = dict(
                width = 2,                                                              #tebal garis
                color = 'red',                                                          #warna garis
            ),
            opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()), #transaparansi garis
        )
    )
    
layout = dict(
        title = 'Jalur Penerbangan',                                            #judul
        showlegend = False,                                                             #legend
        geo = dict(                                                                     #membentuk map
            scope='north america',                                                      #map yang ditampilkan
            projection=dict( type='orthographic' ),                                     #bentuk peta
            countrycolor = '#000',                                                      #warna garis negara
            showland = True,                                                            #tampilkan daratan
            showlakes = True,                                                           #tampilkan danau
            showcountries = True,                                                       #tampilkan garis negara
            showocean = True,                                                           #tampilkan samudera
            countrywidth = 0.5,                                                         #ukuran garis negara
            landcolor = 'rgb(145, 200, 56)',                                            #warna daratan
            lakecolor = 'rgb(0, 255, 255)',                                             #warna danau
            oceancolor = 'rgb(0, 255, 255)',                                            #warna samudera
        ),

    )


fig = dict( data=flight_paths + airports, layout=layout )                               #membuat figure
py.offline.plot( fig, filename='flight_paths.html' )                                    #plot secara offline dan menamakan file .HTML
