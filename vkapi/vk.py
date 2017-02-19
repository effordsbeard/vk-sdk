import urlparse, requests

class VKAPI(object):
    base_url = 'https://api.vk.com/method/'
    method_class = ''
    method = ''
    version = 5.62

    def __init__(self, access_token=''):
        self.access_token = access_token

    def send(self, _params):
        url = urlparse.urljoin(self.base_url, self.method)
        params = {
            'v': self.version,
            'access_token': self.access_token
        }
        params.update(_params)
        try:
            res = requests \
                .get(url, params=params, timeout=20) \
                .json()
            return res
        except:
            return None

    def set_method(self, method):
        self.method = '%s.%s' % (self.method_class, method)

