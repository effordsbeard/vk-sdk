from vk import VKAPI


class Search(VKAPI):
    method_class = 'search'

    def __init__(self, access_token=''):
        super(Search, self).__init__(access_token=access_token)
    
    def get_hints(self, **params):
        self.set_method('getHints')
        return self.send(params)

