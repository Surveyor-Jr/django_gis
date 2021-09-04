from django import forms

class ShapefileForm(forms.Form):
    shapefile = forms.FileField(label='', widget=forms.FileInput(attrs={
        'class': 'form-control',
        'id': 'inputGroupFile02'
    }))