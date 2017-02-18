from vk import VKAPI


class Other(VKAPI):
    method_class = 'other'

    def __init__(self, access_token=''):
        super(Other, self).__init__(access_token=access_token)
    
    def execute(self, **params):
        self.set_method('execute')
        return self.send(params)

