from ag95 import configure_logger
from XT.pyXT import pyXT
from pprint import pprint

if __name__ == '__main__':
    configure_logger()
    # ########### public examples ###########
    # initialize the APi wrapper
    API_obj = pyXT()

    # get the sever time
    pprint(API_obj.get_server_time())