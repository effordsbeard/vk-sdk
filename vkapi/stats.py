from vk import VKAPI


class Stats(VKAPI):
    method_class = 'stats'

    def __init__(self, access_token=''):
        super(Stats, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_post_reach(self, **params):
        self.set_method('getPostReach')
        return self.send(params)

    def track_visitor(self, **params):
        self.set_method('trackVisitor')
        return self.send(params)

