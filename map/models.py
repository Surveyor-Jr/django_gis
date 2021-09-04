from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

class FileType(models.Model):
    name = models.CharField(max_length=200, verbose_name="File Format")
    ext = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Spatial Data File Type'

    def __str__(self):
        return self.name

SHARING_OPTION = [
    ('Private', 'Private'),
    ('Public', 'Public'),
]

class SpatialData(models.Model):
    name = models.CharField(max_length=200)
    fileType = models.ForeignKey(FileType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='spatial_data/%Y/%m/%d')
    tags = TaggableManager()
    short_description = models.CharField(max_length=200, verbose_name='Short Description')
    description = models.TextField()
    terms_of_use = models.TextField()
    sharing = models.CharField(max_length=20, choices=SHARING_OPTION, default='Private')
    slug = models.SlugField(max_length=500, editable=False)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Spatial Data Repository'
        verbose_name_plural = 'Spatial Data Repository'

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name