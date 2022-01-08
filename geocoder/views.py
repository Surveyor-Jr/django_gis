from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import SingleGeocodeForm, BatchGeocodeForm
from .utils import handle_batch_geocode_file, handle_user_address, reverse_geocode_result





def geocode(request):
    if request.method == 'POST':
        form = SingleGeocodeForm(request.POST)
        if form.is_valid():
            try:
                return handle_user_address(request, form)
                
            except:
                context = {
                    'error_message': 'The parameters entered do not match any address on the planet.'
                }
                return render(request, 'error.html', context)

    else:
        form = SingleGeocodeForm()

    context = {
        'form': form,
    }
    return render(request, 'geocoder/single-address-geocode.html', context)



def reverse_geocode(request): 
    if request.method != 'POST':
        return render(request, 'geocoder/reverse_geocode.html')
    return reverse_geocode_result(request)


def batch_geocoding(request):
    if request.method == 'POST':
        form = BatchGeocodeForm(request.POST, request.FILES)
        if form.is_valid():
            return handle_batch_geocode_file(request)
    else:
        form = BatchGeocodeForm()
        context = {
            'form': form
        }

    return render(request, 'geocoder/batch_geocode.html', context)



