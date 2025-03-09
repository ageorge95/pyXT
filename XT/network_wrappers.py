from typing import (AnyStr,
                    Dict,
                    Literal)
from logging import getLogger
from traceback import format_exc
import requests

class API_call:
    def __init__(self,
                 base_url: AnyStr,
                 added_url: AnyStr,
                 data: Dict,
                 headers: Dict = None,
                 max_retries: int = 1,
                 call_method: Literal['GET', 'POST'] = 'GET'):

        self._log = getLogger()
        self.final_URL = base_url + '/' + added_url
        self.max_retries = max_retries
        self.data = data
        self.headers = headers
        self.call_method_description = call_method
        self.call_method_callable = {'GET': requests.get,
                                     'POST': requests.post}[call_method]

    def send(self) -> Dict:

        current_retry = 0
        while current_retry < self.max_retries:
            try:
                self._log.info(f'Sending an API call to {self.final_URL} at retry attempt {current_retry + 1}/{self.max_retries}')
                # remove parameters with no values
                params = dict(filter(lambda _:_[1], {'url': self.final_URL,
                                                     'headers': self.headers,
                                                     'timeout': (5*60,5*60)}.items()))
                if self.call_method_callable is requests.post:
                    params['json'] = self.data
                elif self.call_method_callable is requests.get:
                    params['params'] = self.data
                else:
                    raise Exception(f'Unknown call method {self.call_method_description}')

                return {'API_call_success': True,
                        'data': self.call_method_callable(**params).json()}
            except:
                self._log.error(f'Failed to send an API call to {self.final_URL} at retry attempt {current_retry + 1}/{self.max_retries}')
                current_retry += 1
                self._log.error(format_exc(chain=False))

        return {'API_call_success': False,
                'data': None}
