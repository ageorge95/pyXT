from logging import getLogger
from typing import (AnyStr,
                    List)
from XT.network_wrappers import API_call

class PublicEndpoints():
    _log: getLogger
    base_endpoint: AnyStr

    def __init__(self):
        super(PublicEndpoints, self).__init__()

    def get_server_time(self,
                        max_retries: int = 1):

        added_url = r'v4/public/time'

        data = {}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        max_retries=max_retries).send()

    def get_client_IP(self,
                      max_retries: int = 1):

        added_url = r'v4/public/client'

        data = {}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        max_retries=max_retries).send()

    def get_symbol_information(self,
                               symbol: AnyStr = '',
                               symbols: List[AnyStr] = (),
                               max_retries: int = 1):

        added_url = r'v4/public/symbol'

        if symbol:
            data = {'symbol': symbol}
        elif symbols:
            data = {'symbols': ','.join(symbols)}
        else:
            data = {}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        max_retries=max_retries).send()

    def get_depth_data(self,
                       symbol: AnyStr,
                       limit: int = 100,
                       max_retries: int = 1):

        added_url = r'v4/public/depth'

        data = {'symbol': symbol,
                'limit': min([max([100, limit]), 500])}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        max_retries=max_retries).send()