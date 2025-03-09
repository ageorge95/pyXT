from ag95 import configure_logger
from XT.pyXT import pyXT
from pprint import pprint

if __name__ == '__main__':
    public_key = ''
    private_key = ''

    configure_logger()
    # ########### public examples ###########
    # initialize the APi wrapper
    # API_obj = pyXT()

    # get the sever time
    # pprint(API_obj.get_server_time())

    # get the client IP
    # pprint(API_obj.get_client_IP())

    # get symbol information
    # pprint(API_obj.get_symbol_information(symbol='btc_usdt'))

    # get symbols information
    # pprint(API_obj.get_symbol_information(symbols=['btc_usdt','ai3_usdt']))

    # get depth information
    # pprint(API_obj.get_depth_data(symbol='ai3_usdt',
    #                               limit=100))

    # ########### order examples ###########
    # initialize the APi wrapper
    # API_obj = pyXT(public_key=public_key,
    #                private_key=private_key)

    # get single order data
    # pprint(API_obj.get_single_order(orderId=457101291133639872))

    # submit a market SELL order
    # pprint(API_obj.submit_order(symbol='ai3_usdt',
    #                             side='SELL',
    #                             type='MARKET',
    #                             quantity=20))
    # response example:
    # {'API_call_success': True,
    #  'data': {'ma': [],
    #           'mc': 'SUCCESS',
    #           'rc': 0,
    #           'result': {'clientOrderId': None, 'orderId': '12345'}}}

    # submit a market BUY order
    # pprint(API_obj.submit_order(symbol='ai3_usdt',
    #                             side='BUY',
    #                             type='MARKET',
    #                             quoteQty=6.93))
    # response example:
    # {'API_call_success': True,
    #  'data': {'ma': [],
    #           'mc': 'SUCCESS',
    #           'rc': 0,
    #           'result': {'clientOrderId': None, 'orderId': '12345'}}}


    # ########### balance examples ###########
    # initialize the APi wrapper
    # API_obj = pyXT(public_key=public_key,
    #                private_key=private_key)

    # get the balance of a certain currency
    # pprint(API_obj.get_balance(currency='usdt'))