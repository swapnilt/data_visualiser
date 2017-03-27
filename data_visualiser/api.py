from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization



from data_visualiser.models import (MaxTempData, MinTempData,
                    MeanTempData, RainData, SunshineData)


class MaxTempResource(ModelResource):
    class Meta:
        queryset = MaxTempData.objects.all()
        resource_name = 'maxtemp'
        filtering = {
                     'region':ALL,
                     'year': ALL
                     }
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True 
        authentication = Authentication()
        
        

class MinTempResource(ModelResource):
    class Meta:
        queryset = MinTempData.objects.all()
        resource_name = 'mintemp'
        filtering = {
                     'region':ALL,
                     'year': ALL
                     }
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True 
        authentication = Authentication()
        
class MeanTempResource(ModelResource):
    class Meta:
        queryset = MeanTempData.objects.all()
        resource_name = 'meantemp'
        filtering = {
                     'region':ALL,
                     'year': ALL
                     }
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True 
        authentication = Authentication()
        
class RainDataResource(ModelResource):
    class Meta:
        queryset = RainData.objects.all()
        resource_name = 'raindata'
        filtering = {
                     'region':ALL,
                     'year': ALL
                     }
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True 
        authentication = Authentication()
        
        
class SunshineDataResource(ModelResource):
    class Meta:
        queryset = SunshineData.objects.all()
        resource_name = 'sunshinedata'
        filtering = {
                     'region':ALL,
                     'year': ALL
                     }
        allowed_methods = ['get']
        authorization = Authorization()
        always_return_data = True 
        authentication = Authentication()     
        
                
                        