#! /usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import

import os
import io
import json
import requests

from .client import CoinsBillClient

try:
    basestring
except NameError:
    basestring = str

class Invoice(CoinsBillClient):
    """Handle invoice to the CoinsBill API."""

    INVOICE_ENDPOINT = 'https://www.coinsbill.com/api/invoice'

    def create(self, **params):
        uri = self.BASE_URL + 'invoice/'
        print uri
        data = dict(**(params or {}))
        r = self.client.post(uri, data=json.dumps(data))
        print r.json()

        return r



class ResourceMixin(Invoice):
    """Combined Mixin API."""
    pass


class CoinsBill:

    def __init__(self, api_key):
        self.authorize = CoinsBillClient()
        self.invoice = Invoice(api_key)

    def authorize(self):
        return CoinsBillClient(api_key)

    def invoice(self):
        return self.invoice
