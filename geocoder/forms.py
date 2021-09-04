from django import forms
from .models import SingleAddressGeocode, ReverseGeocode

class SingleGeocodeForm(forms.ModelForm):
    address = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp'
    }))
    class Meta:
        model = SingleAddressGeocode
        fields = ['address', ]

class BatchGeocodeForm(forms.Form):
    file = forms.FileField(label='', widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'inputGroupFile02'
    }))

class ReverseGeocodeForm(forms.ModelForm):
    lat = forms.CharField(label='Latitude', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp'
    }))
    lon = forms.CharField(label='Longitude', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp'
    }))

    class Meta:
        model = ReverseGeocode
        fields = ['lat', 'lon']
