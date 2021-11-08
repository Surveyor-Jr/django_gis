from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import User
from geocoder.models import SingleAddressGeocode
from utility.models import Join, Polar, CoordinateTransform
from .forms import UserRegisterForm

def home(request):
    return render(request, 'users/profile.html')

# user registration 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created. Login now')
            return redirect('profile-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class GeocodeList(ListView):
    model = SingleAddressGeocode
    context_object_name = 'geocode'
    template_name = 'users/single_address_geocode.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return SingleAddressGeocode.objects.filter(user=current_user)


class JoinList(ListView):
    model = Join
    context_object_name = 'join'
    template_name = 'users/calculated_joins.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Join.objects.filter(user=current_user)
    

class PolarList(ListView):
    model = Polar
    context_object_name = 'polar'
    template_name = 'users/calculated_polar.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return Polar.objects.filter(user=current_user)


class CoordinateTransformList(ListView):
    model = CoordinateTransform
    context_object_name = 'coord_transform'
    template_name = 'users/transformed_coords.html'

    # Return results for the authenticated user only
    def get_queryset(self):
        current_user = self.request.user
        return CoordinateTransform.objects.filter(user=current_user)