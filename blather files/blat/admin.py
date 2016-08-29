from django.contrib import admin
from blat.models import Blat

# Register your models here.
class BlatAdmin(admin.ModelAdmin):
	pass

admin.site.register(Blat, BlatAdmin)