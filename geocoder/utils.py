from django.shortcuts import render, redirect
from .models import ReverseGeocode
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium

def containsNumber(value):
    """
    Let's check if the user input for calculating Geodesic distance contains
    Any numerical values
    Warning: Not a best practice so far. 
    """
    return any(character.isdigit() for character in value)


def handle_batch_geocode_file(request):
    """
    This function handles the uploaded CSV file and prepares it for the Batch-Geocoding process
    """
    csv_file = request.FILES['file']
    df = pd.read_csv(csv_file)

    geolocator = Nominatim(user_agent="django_gis")
    # function to delay between geocoding calls
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    # create location column 
    df['location'] = df['Address'].apply(geocode)
    # create lat, lon and alt from location column
    df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
    # split point column into latitude, longitude and altitude columns
    df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)

    df.to_csv(r"geocoded.csv")#TODO:Save file to media route for download or better off be able to just download without saving          

    context = {

    }
    return render(request, 'geocoder/batch_geocode.html', context)


def handle_user_address(request, form):
    """
    This function handles the user's address upon input. Getting the data from the form until it saves incase the users needs their data
    in their database.
    """
    address = request.POST.get('address')
    geolocator = Nominatim(user_agent="django_gis")
    location = geolocator.geocode(address)
    lat = location.latitude
    lon = location.longitude
    address = location.address
    everything = location.raw                
    # the map obj
    m = folium.Map(location=[lat, lon], zoom_start=6)
    # Adding a marker
    folium.Marker(
            [lat, lon],
            tooltip='Click for more info',
            popup=address).add_to(m)
            # the HTML representation
    m = m._repr_html_()

    # Save to the DB
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        instance.lat = lat
        instance.lon = lon
        instance.full_address = address
        instance.metadata = everything
        instance.html_map = m
        instance.user = request.user #Saves to the current logged in users
        instance.save()

    context = {
        'form': form,
        'last_item': address,
        'm': m,
        'lat': lat,
        'lon': lon,
        'everything': everything,
    }

    return render(request, 'geocoder/single-address-geocode.html', context)


def reverse_geocode_result(request):
    """
    A function to handle the Reverse-geocoding requests from the user input. 
    User specifies the Lat and Lon on the earth's grid and function returns the place-name
    """
    lat = request.POST.get('latitude')
    lon = request.POST.get('longitude')
    geolocator = Nominatim(user_agent="django_gis")
    location = geolocator.reverse(f"{lat}, {lon}")
    latitude = location.latitude
    longitude = location.longitude
    address = location.address
    raw = location.raw
    # the map obj
    m = folium.Map(location=[latitude, longitude], zoom_start=6)
    # Adding a marker
    folium.Marker(
        [latitude, longitude],
        tooltip='Click for more info',
        popup=address).add_to(m)
    # the HTML representation
    m = m._repr_html_()

    # Saving the data
    save_data = request.POST.get('saved')
    if save_data == 'on':
        ReverseGeocode.objects.create(lat=lat, lon=lon, latitude=latitude, longitude=longitude, full_address=address, metadata=raw, html_map=m, user=request.user)

    context = {
        'lat': latitude,
        'lon': longitude,
        'address': address,
        'raw': raw,
        'map': m,
    }
    return render(request, 'geocoder/reverse_geocode.html', context)
