from vk import VKAPI


class Storage(VKAPI):
    method_class = 'storage'

    def __init__(self, access_token=''):
        super(Storage, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_keys(self, **params):
        self.set_method('getKeys')
        return self.send(params)

    def set(self, **params):
        self.set_method('set')
        return self.send(params)

