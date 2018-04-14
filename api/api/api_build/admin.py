from django.contrib import admin
from .models import Appliances, Dailyusage, Powerusage, Hvacusage, Rooms, Sensors, Waterusage, Weather

# Register your models here.
admin.site.register(Appliances)
admin.site.register(Dailyusage)
#admin.site.register(Energyusage)
admin.site.register(Hvacusage)
admin.site.register(Powerusage)
admin.site.register(Rooms)
admin.site.register(Sensors)
admin.site.register(Waterusage)
admin.site.register(Weather)