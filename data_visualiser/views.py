from django.shortcuts import render
from django.core.cache import cache
from django.db.models import Max, Min
from data_visualiser.models import (MeanTempData, MinTempData,
            MaxTempData, RainData, SunshineData)
from constants import (DATA_FETCH_COMPLETE, DATA_FETCH_STARTED,
                       DATA_FETCH_STATUS, JOB_ID)
import django_rq
from bg_jobs.fetch_data import job as myjob


def check_job_status():
    # check if job is finished
    job_id = cache.get(JOB_ID)
    if not job_id:
        return 
    q = django_rq.get_queue('default')
    job = q.fetch_job(job_id)
    return job.status


def homepage(request):
    ctx= {
         'data_available': False,
         'in_prog': False
         }
    status = check_job_status()
    if request.method == "GET":
        if status:
            # check if 
            if status == DATA_FETCH_STARTED:
                ctx['in_prog'] = True
            elif status == DATA_FETCH_COMPLETE:
                year_min = MaxTempData.objects.all().aggregate(Min('year'))
                start_year = year_min['year__min']
                year_max = MaxTempData.objects.all().aggregate(Max('year'))
                end_year = year_max['year__max']
                ctx['data_available'] = True
                ctx['years'] = range(start_year, end_year+1)
                
                
    if request.method == "POST":
        if status != DATA_FETCH_STARTED:
            # discard all existing data
            MaxTempData.objects.all().delete()
            MinTempData.objects.all().delete()
            MeanTempData.objects.all().delete()
            RainData.objects.all().delete()
            SunshineData.objects.all().delete()
            # put task in rq queue
            job = django_rq.enqueue(myjob)
            cache.set(JOB_ID, job.id)
            
        
        ctx['in_prog'] = True
        
    return render(request, "homepage.html", context = ctx)




