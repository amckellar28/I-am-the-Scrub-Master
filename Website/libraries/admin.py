from django.contrib import admin
from libraries.models import Library
from libraries.models import Museums, Restaurants,Malls
from libraries.models import Colleges, Industries, Hotels, Parks,Zoos, maps
admin.site.register(Library)
admin.site.register(Colleges)
admin.site.register(Industries)
admin.site.register(Hotels)
admin.site.register(Parks)
admin.site.register(Zoos)
admin.site.register(Museums)
admin.site.register(Restaurants)
admin.site.register(Malls)
admin.site.register(maps)

