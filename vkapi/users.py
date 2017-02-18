from vk import VKAPI


class Users(VKAPI):
    method_class = 'users'

    def __init__(self, access_token=''):
        super(Users, self).__init__(access_token=access_token)
    
    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_followers(self, **params):
        self.set_method('getFollowers')
        return self.send(params)

    def get_nearby(self, **params):
        self.set_method('getNearby')
        return self.send(params)

    def get_subscriptions(self, **params):
        self.set_method('getSubscriptions')
        return self.send(params)

    def is_app_user(self, **params):
        self.set_method('isAppUser')
        return self.send(params)

    def report(self, **params):
        self.set_method('report')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

