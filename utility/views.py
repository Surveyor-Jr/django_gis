from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JoinForm, PolarForm, CoordinateForm
from .models import CoordinateTransform
from .utils import calculate_join, calculate_polar, handle_coordinate_transformation, geodesic_from_coords, geodesic_from_place_name
import folium

def geodesic_distance(request):
    from geopy import distance
    if request.method == 'POST':
        # using coordinates
        return geodesic_from_coords(request)
    else:
        # geocode the name
        return geodesic_from_place_name(request)        
    return render(request, 'utility/distance.html')


def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            return calculate_join(request, form)
    else:
        form = JoinForm

    context = {
        'form': form,
    }

    return render(request, 'utility/join.html', context)


def polar(request):
    if request.method == 'POST':
        form = PolarForm(request.POST)
        if form.is_valid():
            return calculate_polar(request, form)
    else:
        form = PolarForm()

    context = {
        'form': form,
    }

    return render(request, 'utility/polar.html', context)


def coordinate_transform(request):
    if request.method == 'POST':
        form = CoordinateForm(request.POST)
        if form.is_valid():
            return handle_coordinate_transformation(request, form)
    else:
        form = CoordinateForm()

    context = {
        'form': form,
    }


    return render(request, 'utility/coordinate_transform.html', context)

