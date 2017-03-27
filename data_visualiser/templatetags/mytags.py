
from __future__ import unicode_literals
import os.path, time

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders

register = template.Library()




@register.simple_tag()
def mystatic(wfilepath):
    '''
    This tag helps to invalidate client side browser cache when a server side
    static resource eg. js file is updated. It attaches a version string based on
    the last updated timestamp to the file's url.  
    '''
    if settings.DEBUG:
        result = finders.find(wfilepath)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            
            filepath = result[0]
        else:
            wfilepath = settings.STATIC_URL + wfilepath
            return wfilepath
                
    else:
        if settings.STATIC_ROOT:
            rootp = settings.STATIC_ROOT
        else:
            if settings.BASE_DIR:
                rootp = os.path.join(settings.BASE_DIR , "static")
            else:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                rootp = os.path.join(BASE_DIR , "static")
        filepath = os.path.join(rootp, wfilepath)
    
    wfilepath = settings.STATIC_URL + wfilepath
    try:
        mtime = os.path.getmtime(filepath)
        res = wfilepath + "?v=" + str(int(mtime))
    except OSError, e:
        res = wfilepath
    return res
