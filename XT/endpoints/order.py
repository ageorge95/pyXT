from logging import getLogger
from typing import AnyStr, Literal
from XT.network_wrappers import API_call
from XT.utils import (check_API_key,
                      AuthHeaderGenerator)

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
        call_method = 'GET'

        data = {'orderId': orderId}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method=call_method,
                                                                               params=data,
                                                                               data=None),
                        max_retries=max_retries,
                        call_method=call_method).send()

    @check_API_key
    def get_historical_orders(self,
                              symbol: str,
                              order_type: Literal['LIMIT', 'MARKET'],
                              limit: int = 2,
                              max_retries: int = 1):

        added_url = r'v4/history-order'
        call_method = 'GET'

        data = {'symbol': symbol,
                'order_type': order_type,
                'limit': limit}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method=call_method,
                                                                               params=data,
                                                                               data=None),
                        max_retries=max_retries,
                        call_method=call_method).send()

    @check_API_key
    def query_open_order(self,
                         symbol: str,
                         max_retries: int = 1):

        added_url = r'v4/open-order'
        call_method = 'GET'

        data = {'symbol': symbol}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method=call_method,
                                                                               params=data,
                                                                               data=None),
                        max_retries=max_retries,
                        call_method=call_method).send()

    @check_API_key
    def submit_order(self,
                     symbol: str,
                     side: Literal['BUY', 'SELL'],
                     type: Literal['LIMIT', 'MARKET'],
                     bizType: Literal['SPOT', 'LEVER'] = 'SPOT',
                     timeInForce: Literal['GTC', 'FOK', 'IOC', 'GTX'] = 'FOK',
                     price: float | str = None,
                     quantity: float | str = None,
                     quoteQty: float | str = None,
                     max_retries: int = 1):

        '''
        :param symbol:
        :param side:
        :param type:
        :param bizType:
        :param timeInForce:
        GTC (Good 'Til Canceled): The order stays open until it’s filled or you cancel it.
        IOC (Immediate Or Cancel): The order will try to fill immediately;
         any portion that can’t be filled right away is canceled.
        FOK (Fill Or Kill): The order must be filled entirely immediately;
         if it can’t, the whole order is canceled.
        GTX (Good ’Til Crossing): Often used in futures or margin trading, this means the order will
         only be placed if it does not immediately match an existing order—ensuring it only adds
         liquidity (similar to a post-only order).
        :param price:
        :param quantity:
        :param quoteQty:
        :param max_retries:
        :return:
        '''

        added_url = r'v4/order'
        call_method = 'POST'

        if type == 'LIMIT' and not price:
            raise Exception('You selected a LIMIT order type but provided no price !')

        if type == 'MARKET' and side == 'BUY' and not all([not quantity, bool(quoteQty)]):
            raise Exception('You selected a MARKET BUY order type but the parameters are incorrect.'
                            ' quantity must be null and quoteQty must have values')

        if type == 'MARKET' and side == 'SELL' and not all([bool(quantity), not quoteQty]):
            raise Exception('You selected a MARKET SELL order type but the parameters are incorrect.'
                            ' quoteQty must be null and quantity must have values')

        data = {'symbol': symbol,
                'side': side,
                'type': type,
                'bizType': bizType,
                'timeInForce': timeInForce,
                'price': price,
                'quantity': quantity,
                'quoteQty': quoteQty}

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data=data,
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method=call_method,
                                                                               params=None,
                                                                               data=data),
                        max_retries=max_retries,
                        call_method=call_method).send()

    @check_API_key
    def cancel_order(self,
                     orderId: int,
                     max_retries: int = 1):

        added_url = fr'v4/order/{orderId}'
        call_method = 'DELETE'

        return API_call(base_url=self.base_endpoint,
                        added_url=added_url,
                        data={},
                        headers=AuthHeaderGenerator(self.public_key,
                                                    self.private_key).generate(url=added_url,
                                                                               method=call_method,
                                                                               params=None,
                                                                               data={}),
                        max_retries=max_retries,
                        call_method=call_method).send()