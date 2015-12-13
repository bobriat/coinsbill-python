# CoinsBill Python bindings 


This is a simple library for interacting with the [Vimeo API](https://developers.vimeo.com).

### Example Usage

```python
from coinsbill import CoinsBill
access_token = 'a9esthaVUjOuvzTCSTXsJUCK0lCMCk'
c = CoinsBill(access_token)

invoices = c.invoice.get('/invoice')

new = c.invoice.create( 
    email="bill@dow.com",
    currency="USD",
    country="US",
    billing_first_name="Sam",
    items=[{ "name": "api Name", "quantity": 10, "unit_price": 2}, { "name": "api 2", "quantity": "4", "unit_price": 3 }] 
    )




assert invoices.status_code == 200  # Make sure we got back a successful response.
print invoices.json()   # Load the body's JSON data.

```

Note:  You can find the app tokens and an authenticated bearer token on Dashboard at the [CoinsBill Dashboard](https://www.coinsbill.com/dashboard).

### Installation 

This package is called ``coinsbill`` on PyPI. Install using::

    $ pip install --upgrade  coinsbill















