from django.http import request
from django.shortcuts import render
from django.views.generic import ListView
from geocoder.models import SingleAddressGeocode, ReverseGeocode

def home(request):
    return render(request, 'users/profile.html')

class GeocodeList(ListView):
    model = SingleAddressGeocode
    context_object_name = 'geocode'
    template_name = 'users/single_address_geocode.html'

    # def get_context_data(self, **kwargs):
    #     context = super(SingleAddressGeocode, self).get_context_data(**kwargs)
    #     context['count'] = self.get_queryset().count()
    #     return context
