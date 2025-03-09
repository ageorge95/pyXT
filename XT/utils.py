import time
import json
import hmac
import hashlib

def check_API_key(func):
    def inner(*args, **kwargs):
        if not args[0].public_key or not args[0].private_key:
            args[0]._log.error(f'{func.__name__} requires an API key and API secret!')
        return func(*args, **kwargs)
    return inner

class AuthHeaders:
    def __init__(self,
                 url,
                 method,
                 public_key,
                 private_key,
                 params = None,
                 data = None,
                 json = None):
        self.url = url
        self.method = method
        self.public_key = public_key
        self.private_key = private_key
        self.params = params
        self.data = data
        self.json = json

    def create_sign(self,
                    headers):
        data = self.data or self.json
        query_str = '' if self.params is None else '&'.join(
            [f"{key}={json.dumps(self.params[key]) if type(self.params[key]) in [dict, list] else self.params[key]}" for key in
             sorted(self.params)])  # 没有接口同时使用query和body
        body_str = json.dumps(data) if data is not None else ''

        y = '#' + '#'.join([i for i in [self.method, f'/{self.url}/', query_str, body_str] if i])
        x = '&'.join([f"{key}={headers[key]}" for key in sorted(headers)])
        sign = f"{x}{y}"

        return hmac.new(self.private_key.encode('utf-8'), sign.encode('utf-8'),
                        hashlib.sha256).hexdigest().upper()

    def gen_auth_header(self):
        headers = {'validate-algorithms': 'HmacSHA256',
                   'validate-appkey': self.public_key,
                   'validate-recvwindow': str(60000),
                   'validate-timestamp': str(int((time.time() - 30) * 1000)),
                   }
        headers |= {'validate-signature': self.create_sign(headers=headers)}
        return headers

class AuthHeaderGenerator:
    def __init__(self,
                 access_key: str,
                 secret_key: str,
                 recv_window: str = '60000'):
        """
        :param access_key: Your API access key.
        :param secret_key: Your API secret key.
        :param recv_window: Receive window in milliseconds (default '60000').
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.recv_window = recv_window

    def generate(self,
                 url: str,
                 method: str,
                 params: dict = None,
                 data: dict = None) -> dict:
        """
        Generate authentication headers for the API request.

        :param url: API endpoint URL (the path portion).
        :param method: HTTP method, e.g., 'GET' or 'POST'.
        :param params: Optional query parameters (dict).
        :param data: Optional JSON body data (dict).
        :return: Dictionary of headers to include in the request.
        """
        # Create the base headers.
        headers = {
            'xt-validate-timestamp': str(int((time.time() - 30) * 1000)),
            'xt-validate-appkey': self.access_key,
            'xt-validate-recvwindow': self.recv_window,
            'xt-validate-algorithms': 'HmacSHA256'
        }

        # Build the query string (if any) sorted by key.
        query_str = ''
        if params:
            query_str = '&'.join(
                f"{k}={json.dumps(params[k]) if isinstance(params[k], (dict, list)) else params[k]}"
                for k in sorted(params)
            )

        # Build the body string (if any).
        body_str = json.dumps(data) if data else ''

        # Concatenate method, URL, query string, and body string with delimiters.
        sign_data = '#' + '#'.join(item for item in [method, '/' + url, query_str, body_str] if item)

        # Build the header string (sorted by key).
        header_str = '&'.join(f"{k}={headers[k]}" for k in sorted(headers))

        # The final string to sign.
        string_to_sign = f"{header_str}{sign_data}"

        # Generate the HMAC-SHA256 signature.
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            string_to_sign.encode('utf-8'),
            hashlib.sha256
        ).hexdigest().upper()

        # Add signature to headers.
        headers['xt-validate-signature'] = signature

        return headers

# Example usage:
if __name__ == "__main__":
    access_key = "your-access-key"
    secret_key = "your-secret-key"
    url = "/spot/v4/order"  # The endpoint path
    method = "POST"
    params = None  # or {"symbol": "BTC_USDT", ...} if needed
    data = {
        "symbol": "BTC_USDT",
        "clientOrderId": "16559390087220001",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "bizType": "SPOT",
        "price": 20,
        "quantity": 0.001
    }

    auth_gen = AuthHeaderGenerator(access_key, secret_key)
    headers = auth_gen.generate(url, method, params=params, data=data)
    print("Authentication Headers:\n",headers)