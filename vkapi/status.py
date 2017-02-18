from vk import VKAPI


class Status(VKAPI):
    method_class = 'status'

    def __init__(self, access_token=''):
        super(Status, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def set(self, **params):
        self.set_method('set')
        return self.send(params)

