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
    #                               limit=2))
    # response example:
    # {'API_call_success': True,
    #  'data': {'ma': [],
    #           'mc': 'SUCCESS',
    #           'rc': 0,
    #           'result': {'asks': [['0.3615', '54.65'],
    #                               ['0.3616', '36.56'],
    #                               ['1.4998', '53.23'],
    #                               ['1.4999', '50.00']],
    #                      'bids': [['0.3471', '337.65'],
    #                               ['0.3468', '2578.73'],
    #                               ['0.0453', '327.20'],
    #                               ['0.0168', '764.54']],
    #                      'lastUpdateId': 1741313703530,
    #                      'symbol': 'ai3_usdt',
    #                      'timestamp': 1741541010718}}}

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

    # result example:
    # {'API_call_success': True,
    #  'data': {'ma': [],
    #           'mc': 'SUCCESS',
    #           'rc': 0,
    #           'result': {'availableAmount': '0.00489971',
    #                      'convertBtcAmount': '0.00000005',
    #                      'convertUsdtAmount': '0.004899718',
    #                      'copyTrade': '0.00000000',
    #                      'currency': 'usdt',
    #                      'currencyId': 11,
    #                      'freeze': '0.00000000',
    #                      'frozenAmount': '0.00000000',
    #                      'lock': '0.00000000',
    #                      'totalAmount': '0.00489971',
    #                      'trade': '0.00000000',
    #                      'withdraw': '0.00000000'}}}