
import urllib2
from bs4 import BeautifulSoup
from utils import rate_limited
from bg_jobs.csv_parser import CSVParser, HEADERS
from data_visualiser.models import MaxTempData, MinTempData, MeanTempData,\
    SunshineData, RainData
from django.core.cache import cache
from data_visualiser.constants import DATA_FETCH_STATUS, DATA_FETCH_COMPLETE

URL = "http://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36"

LANG = 'en-US,en;q=0.8'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

REGIONS = ["UK", "England", "Wales", "Scotland"]
DATE_ORDER = "Date"
RANK_ORDER = "Ranked"

ORDER_TYPE = DATE_ORDER  
MODEL_MAP = {"Tmax": MaxTempData, 
             "Tmin": MinTempData, 
             "Tmean": MeanTempData, 
             "Sunshine": SunshineData, 
             "Rainfall": RainData
             }




@rate_limited
def make_request(url):
    headers = {'Accept-Language': LANG, 
               'Accept': ACCEPT, 
               'User-Agent': USER_AGENT}
    req = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(req)
    return res
    


def get_data(region, order, data_type):
    res = make_request(URL)
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
    title = " ".join([region, order, data_type])
    tag = soup.find("a", title = title)
    file_link = tag['href']
    res = make_request(file_link)
    parser = CSVParser()
    return parser.parse(res)
    
    
def job():
    for region in REGIONS:
        for data_type in MODEL_MAP.keys():
            model = MODEL_MAP[data_type]
            parsed_data = get_data(region, ORDER_TYPE, data_type)
            data_objects = []
            for row in parsed_data:
                year = row[0]
                for i in xrange(1,13):
                    month = HEADERS[i];
                    value = row[i]
                    data_objects.append(model(month = month, value = value,
                                              year = year, region = region))
                
            model.objects.bulk_create(data_objects)
    
    cache.set(DATA_FETCH_STATUS, DATA_FETCH_COMPLETE)
    

    