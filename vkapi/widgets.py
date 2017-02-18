from vk import VKAPI


class Widgets(VKAPI):
    method_class = 'widgets'

    def __init__(self, access_token=''):
        super(Widgets, self).__init__(access_token=access_token)
    
    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def get_pages(self, **params):
        self.set_method('getPages')
        return self.send(params)

