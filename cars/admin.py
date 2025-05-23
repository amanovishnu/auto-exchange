from django.contrib import admin
from django_select2.forms import Select2MultipleWidget
from .models import Car, CarFeature
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):

  def thumbnail(self, object):
    return format_html(f'<img src="{object.car_photo.url}" width="30px" style="border-radius:5px"/>')

  thumbnail.short_description = 'Car Photo'

  formfield_overrides = {
    models.ManyToManyField: {'widget': Select2MultipleWidget}
  }

  list_display = ['id', 'car_title', 'thumbnail', 'model', 'price', 'body_style', 'engine', 'transmission', 'miles', 'fuel_type', 'is_featured']
  search_fields = ['car_title', 'model', 'price', 'engine', 'transmission', 'miles', 'fuel_type']
  list_display_links = ['car_title', 'thumbnail']
  list_filter = ['transmission','fuel_type', 'body_style']
  list_editable = ['is_featured']


# Register your models here.
admin.site.register(Car, CarAdmin)
admin.site.register(CarFeature)
