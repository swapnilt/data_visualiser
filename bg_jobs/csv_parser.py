import csv
import re

HEADERS = ['Year', 
           'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
           'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

DELIMITER = "  "

class CSVParser(object):
    
    def __init__(self):
        self.result = []
    
    def parse(self, file):
        ''' Accepts an open file object and
        Returns a list of dictionary objects '''
        #reader = csv.reader(file, delimiter=' ', skipinitialspace=True)
        header_row = "    ".join(HEADERS)
        headers = []
        start = False
        for row in file:
            row = row.strip().strip("\n").strip("\r")
            if not row:
                continue
            
            if not start:           
                if row.startswith(header_row):
                    start = True    # start parsing from next row
                    continue
                else:
                    continue       # skip initial text until headers row is found
                    
            else:
                
                # extract data
                m = re.match("(\d{4})(.+)", row)
                if m:
                    groups =  m.groups()
                    d1 =  groups[0]
                    d2 =  groups[1]
                    val_list = [d1]
                    def myfunc(matchobj):
                        value = matchobj.groups()[0]
                        try:
                            value = float(value.strip())
                        except ValueError:
                            # handle empty values
                            value = 0.0
                        val_list.append(value)
                    
                    
                    re.sub('  (.{5})', myfunc, d2)
                    self.result.append(tuple(val_list))
                
        return self.result
                    

                    
                
            
            