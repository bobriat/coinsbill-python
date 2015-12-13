import json
import requests



class APIClient(object):
    BASE_URL = 'https://www.coinsbill.com/api/'
    
    def __init__(self, api_key=None, rate_limit_lock=None):
        self.client = requests.session()
        self.client.headers = {
            "Authorization": "bearer %s" % api_key,
            "Content-Type": "application/json",
        } 
        
        self.rate_limit_lock = rate_limit_lock

    def _compose_url(self, path, params=None):
        # return self.BASE_URL + path + '?' + urlencode(params)
        return self.BASE_URL + path 

    def _handle_response(self, response):
        
        return response.json()


    def status(self, response):
        return response.status_code

    def _request(self, method, path, **params ):
        uri = self._compose_url(path, params)
        
        self.rate_limit_lock and self.rate_limit_lock.acquire()

        data = dict(**(params or {}))

        if params:
            data.update(params)
        
        
        if method == "POST":
            response = self.client.post(uri, data=json.dumps(data))
            
        elif method == "PUT":    
            response = self.client.put(uri, data=json.dumps(data))
            
        elif method == "GET": 
            response = self.client.get(uri, data=json.dumps(data))
            
        else:
            pass

        return self._handle_response(response)

    def get(self, path, **params):
        return self._request('GET', path, **params)

    def create(self, path, **params):
        return self._request('POST', path, **params)

    def update(self, path, **params):
        return self._request('PUT', path, **params)

    def _call(self, path, **params):
        return self._request('GET', path, params=params)

    


