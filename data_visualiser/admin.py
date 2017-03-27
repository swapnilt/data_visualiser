from django.contrib import admin
from data_visualiser.models import (MaxTempData, MinTempData, 
                    MeanTempData, RainData, SunshineData)


class DataAdmin(admin.ModelAdmin):
    list_display = ['region', 'year', 'month', 'value']


admin.site.register(MaxTempData, DataAdmin)
admin.site.register(MinTempData, DataAdmin)
admin.site.register(MeanTempData, DataAdmin)
admin.site.register(SunshineData, DataAdmin)
admin.site.register(RainData, DataAdmin)