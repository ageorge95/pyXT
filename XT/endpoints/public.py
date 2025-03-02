from logging import getLogger
from typing import (AnyStr,
                    List,
                    Literal)
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