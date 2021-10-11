from django.forms import fields, forms, ModelForm, widgets
from django import forms
from .models import Join, Polar, CoordinateTransform, FromShapefile

class JoinForm(ModelForm):
    start_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp',
        'id': 'start_name',
        'placeholder': "Start Point Name"
        
    }))
    y_start = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control col-auto g-3',
        'aria-describedby': 'placeHelp',
        'id': 'y_start',
        'placeholder': 'Y-Coordinate (start-point)',
        'type': 'number'
    }))
    y_end = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control col-auto g-3',
        'aria-describedby': 'placeHelp',
        'id': 'y_end',
        'placeholder': 'Y-Coordinate (end-point)',
        'type': 'number'
    }))
    x_start = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp',
        'id': 'x_start',
        'placeholder': 'X-Coordinate (start-point)',
        'type': 'number'
    }))
    x_end = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp',
        'id': 'x_end',
        'placeholder': 'X-Coordinate (end-point)',
        'type': 'number'
    }))
    end_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp',
        'id': 'end_name',
        'placeholder': 'End Point Name'
    }))

    class Meta:
        model = Join
        fields = ('start_name', 'y_start', 'x_start', 'end_name', 'y_end', 'x_end')


class PolarForm(ModelForm):
    station_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp',
        'id': 'start_name',
        'placeholder': "Station Name"
        
    }))
    x = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'aria-describedby': 'placeHelp',
        'id': 'x',
        'placeholder': 'X-Coordinate',
    }))
    y = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp',
        'id': 'y',
        'placeholder': 'Y-Coordinate',
    }))
    distance = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp',
        'id': 'distance',
        'placeholder': 'Distance',
    }))
    direction = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'aria-describedby': 'placeHelp',
        'id': 'direction',
        'placeholder': 'Direction (eg. 231.54.23)',
        'type': 'text'
    }))
    end_name = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-2',
        'aria-describedby': 'placeHelp',
        'id': 'start_name',
        'placeholder': "End Point Name"
    }))

    class Meta:
        model = Polar
        fields = ('station_name', 'x', 'y', 'distance', 'direction', 'end_name')


class CoordinateForm(ModelForm):
    x = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': "Longitude / X"
    }))
    y = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={
        'class': 'form-control mt-3 mb-3',
        'placeholder': "Latitude / Y"
    }))

    class Meta:
        model = CoordinateTransform
        fields = ('from_epsg', 'y', 'x', 'to_epsg')

class FromShapefileForm(ModelForm):
    file = forms.FileField(required=True, label='Upload Shapefile (.shp)')
    class Meta:
        model = FromShapefile
        fields = ('file',)