from django.contrib import messages
from django.shortcuts import render, redirect
from django.http.response import Http404
from pyproj import CRS, Transformer
from geopy.geocoders import Nominatim
import math
import folium

def join_distance(y_end, y_start, x_end, x_start):
    """
    Calculate the distance between a set of coordinates 
    Given 2 Coordinate Pairs each containing Y and X values
    """
    y_dif = float(y_end) - float(y_start)
    x_dif = float(x_end) - float(x_start)
    return math.sqrt(math.pow(y_dif, 2) + math.pow(x_dif, 2))

def join_direction(y_end, y_start, x_end, x_start):
    """
    Calculate the bearing/direction from the start point to the 
    end point given two coordinate pairs with X and Y values
    """
    y_dif = float(y_end) - float(y_start)
    x_dif = float(x_end) - float(x_start)
    # Calculate Initial Angle
    angle = math.atan2(y_dif, x_dif)

    # Find the Quadrant 

    # 2nd Quad
    if x_dif < 0 < y_dif or x_dif < 0 and y_dif < 0:
        quad = 180

    elif x_dif > 0 > y_dif:
        quad = 360

    else:
        quad = 0

    return math.degrees(angle) + int(quad)

def to_dms(direction):
    """
    convert decimal degrees to deg-min-sec
    based on the Float value of the direction
    """
    degree = int(direction)
    minutes_float = (direction - degree) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60

    return degree, minutes, seconds


def polar_calculation(direction, distance, x, y): 
    """ 
    Calculate a polar ...
    Split the direction into Degrees, Minutes and Seconds based on the separator (.)
    Given only the input value of direction in the format deg.min.sec (i.e -> 123.45.21)
    After the direction is split.. then convert it to decimal degrees for calculation preparation
    Calculate the coordinates of the points (X, y)
    """
    dir = direction.split('.', 2)
    # degrees
    deg = dir[0]
    # minutes
    min = dir[1]
    # seconds
    sec = dir[2]

    # convert into decimal degrees
    dec_deg = int(deg) + (float(min)/60) + (float(sec)/3600)

    # calculate X-Coordinates
    # FIXME: Make sure calculation works well
    x_coordinate = float(x) + (float(distance) * math.degrees(math.cos(dec_deg)))
    y_coordinate = float(y) + (float(distance) * math.degrees(math.sin(dec_deg)))

    return y_coordinate, x_coordinate


# Calculating the Join from Input
def calculate_join(request, form):
    y_start = request.POST.get('y_start')
    x_start = request.POST.get('x_start')
    y_end = request.POST.get('y_end')
    x_end = request.POST.get('x_end')
    # calculate distance
    distance = join_distance(y_end, y_start, x_end, x_start)
    # calculate direction
    direction = join_direction(y_end, y_start, x_end, y_end)
    # convert into DMS
    dms = to_dms(direction)
    # Save to Database
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        instance.distance = distance
        instance.direction_dd = direction
        instance.direction_deg = dms[0]
        instance.direction_min = dms[1]
        instance.direction_sec = dms[2]
        instance.user = request.user # Save result to user profile
        instance.save()
        messages.success(request, "Join computation complete and data stored successfully")

    context = {
        'form': form,
        'distance': distance,
        'direction': direction,
        'degree': dms[0],
        'minutes': dms[1],
        'seconds': dms[2]
    }
    return render(request, 'utility/join.html', context)



# User Input for Polar
def calculate_polar(request, form):
    x = request.POST.get('x')
    y = request.POST.get('y')
    direction = request.POST.get('direction')
    distance = request.POST.get('distance')

    # calculate polar
    polar = polar_calculation(direction, distance, x, y)
    y_coordinate = polar[0]
    x_coordinate = polar[1]

    # Save to Database
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        instance.x_coordinate = polar[1]
        instance.y_coordinate = polar[0]
        instance.user = request.user # Save result to user profile
        instance.save()
        messages.success(request, "Coordinates calculated and stored successfully")

    context = {
        'form': form,
        'y': y_coordinate,
        'x': x_coordinate,
    }

    return render(request, 'utility/polar.html', context)


# User-Input for Coordinate Transformation
def handle_coordinate_transformation(request, form):
    from_epsg = request.POST.get('from_epsg')
    y = request.POST.get('y')
    x = request.POST.get('x')
    to_epsg = request.POST.get('to_epsg')
    # Transform Coordinates
    transformer = Transformer.from_crs(int(from_epsg), int(to_epsg))
    transformed = transformer.transform(y, x)
    # Get transformation parameters
    crs_from_info = CRS.from_epsg(from_epsg)
    crs_to_info = CRS.from_epsg(to_epsg)
    from_parameter = crs_from_info.to_wkt(pretty=True)
    to_parameter = crs_to_info.to_wkt(pretty=True)
    # Save to Database? 
    save_data = request.POST.get('saved')
    if save_data == 'on':
        instance = form.save(commit=False)
        # instance as defined in Model Name
        instance.x_trans = transformed[1]
        instance.y_trans = transformed[0]
        instance.user = request.user # Save result to user profile
        instance.save()
        # form.save()
        messages.success(request, "Coordinate Transormation data stored")

    context = {
        'form': form,
        'y': transformed[0],
        'x': transformed[1],
        'p_from': from_parameter,
        'p_to': to_parameter,
    }

    return render(request, 'utility/coordinate_transform.html', context)


def geodesic_from_coords(request):
    from geopy import distance
    start_lat = request.POST.get('start_lat')
    start_lon = request.POST.get('start_lon')
    end_lat = request.POST.get('end_lat')
    end_lon = request.POST.get('end_lon')
    ellipsoid = request.POST.get('ellipsoid')
    try:
        start = (start_lat, start_lon)
        end = (end_lat, end_lon) 
        # get the ellipsoid

        # get the distance
        distance = distance.distance(start, end, ellipsoid=ellipsoid).km

        # the map obj
        m = folium.Map(location=[start_lat, start_lon], zoom_start=2)
        # Adding a marker for Point A
        folium.Marker(
            [start_lat, start_lon],
            tooltip='Click for more info',
            popup=f"Lat: {start_lat} Lon: {start_lon}").add_to(m)
            
        # Adding a marker for Point B
        folium.Marker(
            [end_lat, end_lon],
            tooltip='Click for more info',
            popup=f"Lat: {end_lat} Lon: {end_lon}").add_to(m)
        # the HTML representation
        m = m._repr_html_()
        context = {
            'distance': distance,
            'map': m,
            'ellipsoid': ellipsoid,
            }
        return render(request, 'utility/distance.html', context)

    except:
            Http404('Something went wrong')

def geodesic_from_place_name(request):
    from geopy import distance
    try:
        start_name = request.GET.get('start_name')
        end_name = request.GET.get('end_name')

        # geocode the names
        geolocator = Nominatim(user_agent="django_gis")
        start_location = geolocator.geocode(start_name)
        end_location = geolocator.geocode(end_name)
        # Start Location Coordinates
        start_lat = start_location.latitude
        start_lon = start_location.longitude
        # End Location Coordinates
        end_lat = end_location.latitude
        end_lon = end_location.longitude

        start = (start_lat, start_lon)
        end = (end_lat, end_lon) 
        # get the distance
        distance = distance.distance(start, end).km

        # the map obj
        m = folium.Map(location=[start_lat, start_lon], zoom_start=2)
        # Adding a marker for Point A
        folium.Marker(
            [start_lat, start_lon],
            tooltip='Click for more info',
            popup=f"Lat: {start_lat} Lon: {start_lon}").add_to(m)
            
        # Adding a marker for Point B
        folium.Marker(
            [end_lat, end_lon],
            tooltip='Click for more info',
            popup=f"Lat: {end_lat} Lon: {end_lon}").add_to(m)

        # define line
        loc = [(start_lat, start_lon),
                (end_lat, end_lon)
            ]

        # connect the points with line
        folium.PolyLine(loc,
                color='black',
                opacity=0.8).add_to(m)
        # the HTML representation
        m = m._repr_html_()

        context = {
            'distance': distance,
            'map': m,
        }
        return render(request, 'utility/distance.html', context)

    except:
            Http404('Something Went Wrong')            
