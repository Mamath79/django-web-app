from django.contrib import admin
from listings.models import Band
from listings.models import Title


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')

class listingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'description', 'year')

admin.site.register(Band, BandAdmin, )
admin.site.register(Title, listingsAdmin)

# Register your models here.
