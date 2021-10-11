from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import JoinForm, PolarForm, CoordinateForm, FromShapefileForm
from .models import CoordinateTransform
from .utils import calculate_join, calculate_polar, handle_coordinate_transformation, geodesic_from_coords, geodesic_from_place_name
import folium

def geodesic_distance(request):
    #FIXME:Acting up weird with heavy bugs needs serious fixing 
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

class ConversionHome(TemplateView):
    template_name = 'utility/conversion_home.html'

def fromShapefile(request):
    if request.method == 'POST':
        form = FromShapefileForm(request.POST, request.FILES)
        convert_to = request.POST.get('convert_to')
        if form.is_valid():
            # Let's do something fun before saving
            form.save()

            context = {
                'form':form,
                'format': convert_to,
            }

            return render(request, 'utility/from_shapefile.html', context)
    
    else:
        form = FromShapefileForm()

    context = {
        'form': form,
    }
    return render(request, 'utility/from_shapefile.html', context)

