from logging import getLogger
from typing import AnyStr
from XT.network_wrappers import API_call
from XT.utils import (check_API_key,
                      AuthHeaderGenerator)
import requests

class BalanceEndpoints():
    _log: getLogger
    base_endpoint: AnyStr
    public_key: AnyStr
    private_key: AnyStr

    def __init__(self):
        super(BalanceEndpoints, self).__init__()

    @check_API_key
    def get_balance(self,
                    currency: AnyStr,
                    max_retries: int = 1):

        added_url = r'v4/balance'

        data = {'currency': currency}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method='GET',
                                                                               params=data,
                                                                               data=None),
                        max_retries=max_retries,
                        call_method=requests.get).send()
