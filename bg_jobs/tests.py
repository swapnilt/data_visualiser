from django.test import TestCase
from bg_jobs.fetch_data import CSVParser
import pdb
from pprint import pprint

HEADERS = ['Year', 
           'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
           'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',
           'WIN', 'SPR', 'SUM', 'AUT', 'ANN']

class CSVParserTestCase(TestCase):
    
    def test_parser(self):
        parser = CSVParser()
        result = []
        with open("UK.txt") as csvfile:
            #pdb.set_trace()
            result = parser.parse(csvfile)
            for res in result:
                print res
        
            