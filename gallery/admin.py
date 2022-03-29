from django.contrib import admin
from .models import Image,Category,Location, Editor

# Register your models here.
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)