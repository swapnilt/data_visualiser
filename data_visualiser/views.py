from django.shortcuts import render
from django.core.cache import cache
from data_visualiser.models import (MeanTempData, MinTempData,
            MaxTempData, RainData, SunshineData)
from constants import (DATA_FETCH_COMPLETE, DATA_FETCH_STARTED,
                       DATA_FETCH_STATUS)
import django_rq
from bg_jobs.fetch_data import job

def homepage(request):
    ctx= {
         'data_available': False,
         'in_prog': False
         }
    status = cache.get(DATA_FETCH_STATUS)
    if request.method == "GET":
        if status:
            # check if 
            if status == DATA_FETCH_STARTED:
                ctx['in_prog'] = True
            elif status == DATA_FETCH_COMPLETE:
                ctx['data_available'] = True
                
    if request.method == "POST":
        if status != DATA_FETCH_STARTED:
            # discard all existing data
            MaxTempData.objects.all().delete()
            MinTempData.objects.all().delete()
            MeanTempData.objects.all().delete()
            RainData.objects.all().delete()
            SunshineData.objects.all().delete()
            # put task in rq queue
            django_rq.enqueue(job)
            # update status
            cache.set(DATA_FETCH_STATUS, DATA_FETCH_STARTED)
            ctx['in_prog'] = True
        
    return render(request, "homepage.html", context = ctx)