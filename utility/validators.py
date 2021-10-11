from django.core.exceptions import ValidationError

def validate_shapefile(value):
    """
    Given an uploaded file. Check to see if it is a Shapefile format with .shp extension
    """
    if not value.name.endswith('.shp'):
            raise ValidationError(u'The Uploaded File is not a Shapefile.')