from vk import VKAPI


class Notifications(VKAPI):
    method_class = 'notifications'

    def __init__(self, access_token=''):
        super(Notifications, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def mark_as_viewed(self, **params):
        self.set_method('markAsViewed')
        return self.send(params)

