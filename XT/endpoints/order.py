from logging import getLogger
from typing import AnyStr
from XT.network_wrappers import API_call
from XT.utils import (check_API_key,
                      AuthHeaderGenerator)
import requests

class OrderEndpoints():
    _log: getLogger
    base_endpoint: AnyStr
    public_key: AnyStr
    private_key: AnyStr

    def __init__(self):
        super(OrderEndpoints, self).__init__()

    @check_API_key
    def get_single_order(self,
                         orderId: int,
                         max_retries: int = 1):

        added_url = r'v4/order'

        data = {'orderId': orderId}

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
