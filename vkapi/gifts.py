from vk import VKAPI


class Gifts(VKAPI):
    method_class = 'gifts'

    def __init__(self, access_token=''):
        super(Gifts, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

