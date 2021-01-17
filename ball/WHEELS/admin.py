from django.contrib import admin
from .models import *


admin.site.register(Wheel)
admin.site.register(Color)
admin.site.register(CountryModel)
admin.site.register(RegionModel)
admin.site.register(RegionChildModel)
admin.site.register(Caliber)
admin.site.register(HolesQty)
admin.site.register(ContactCode)


