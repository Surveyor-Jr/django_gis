from django.http.response import Http404
from django.shortcuts import render, redirect
from .forms import ShapefileForm
from .models import SpatialData, FileType
import folium
# import geopandas as gpd


def map_shapefile(request): # FIXME: Ability to choose file of choice to upload
    if request.method == 'POST':
        form = ShapefileForm(request.POST, request.FILES)
        if form.is_valid():
            shapefile = request.FILES['shapefile']
            # read the shapefile
            # data = gpd.read_file(shapefile) 
            # convert data to GeoJSON
            # data_gjson = folium.features.GeoJson(data, name="Uploaded Shape-file")

            # create map instance
            m = folium.Map(location=[-19.546, 31.546], zoom_start=4, control_scale=True)
            # add points to map 
            folium.GeoJson(shapefile, name='Uploaded File').add_to(m)
            # layer control
            folium.LayerControl().add_to(m)
            # the HTML representation
            m = m._repr_html_()

            context = {
                'map': m,
            }

            return render(request, 'maps/map_shapefile.html', context)

    else:
        form = ShapefileForm()
        context = {
            'form': form
        }
    return render(request, 'maps/map_shapefile.html', context)


def stored_file(request):
    shapefile = SpatialData.objects.all().last().file.url
    shapefile = f"http://localhost:8000{shapefile}" # FIXME Find better method to get full url path

    # create map instance
    m = folium.Map(location=[-19.546, 31.546], zoom_start=4, control_scale=True)
    # add data to map 
    folium.GeoJson(shapefile, name=SpatialData.objects.all().last().name).add_to(m)
    # layer control
    folium.LayerControl().add_to(m)
    # the HTML representation
    m = m._repr_html_()

    context = {
                'map': m,
            }

    return render(request, 'maps/stored_file.html', context)




"""
TODO:
1. Store Coordinates with Names and Plot on Map as Points
2. Store Corner Points and Display as Polygons 

"""
