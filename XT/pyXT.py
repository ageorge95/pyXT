from logging import getLogger
from typing import AnyStr
from XT.endpoints.public import PublicEndpoints

base_endpoint: AnyStr = 'https://sapi.xt.com'

class pyXT(PublicEndpoints):

    def __init__(self,
                 API_key: AnyStr = None,
                 API_secret: AnyStr = None,
                 API_passphrase: AnyStr = None):

        self._log = getLogger()
        self.API_key = API_key
        self.API_secret = API_secret
        self.API_passphrase = API_passphrase

        self.base_endpoint = base_endpoint

        super(pyXT, self).__init__()
