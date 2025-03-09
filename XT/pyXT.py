from logging import getLogger
from typing import AnyStr
from XT.endpoints.public import PublicEndpoints
from XT.endpoints.order import OrderEndpoints
from XT.endpoints.balance import BalanceEndpoints

base_endpoint: AnyStr = 'https://sapi.xt.com'

class pyXT(PublicEndpoints,
           OrderEndpoints,
           BalanceEndpoints):

    def __init__(self,
                 public_key: AnyStr = None,
                 private_key: AnyStr = None):

        self._log = getLogger()
        self.public_key = public_key
        self.private_key = private_key

        self.base_endpoint = base_endpoint

        super(pyXT, self).__init__()
