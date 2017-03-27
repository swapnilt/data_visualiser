import time


RATE_LIMIT = 5  # waits for 5 seconds before making request

def rate_limited(func):
    
    def myfunc(*args, **kwargs):
        time.sleep(RATE_LIMIT)
        res = func(*args, **kwargs)
        return res
    
    return myfunc
    
    