from vk import VKAPI


class Utils(VKAPI):
    method_class = 'utils'

    def __init__(self, access_token=''):
        super(Utils, self).__init__(access_token=access_token)
    
    def check_link(self, **params):
        self.set_method('checkLink')
        return self.send(params)

    def get_server_time(self, **params):
        self.set_method('getServerTime')
        return self.send(params)

    def resolve_screen_name(self, **params):
        self.set_method('resolveScreenName')
        return self.send(params)

