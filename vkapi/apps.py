from vk import VKAPI


class Apps(VKAPI):
    method_class = 'apps'

    def __init__(self, access_token=''):
        super(Apps, self).__init__(access_token=access_token)
    
    def delete_app_requests(self, **params):
        self.set_method('deleteAppRequests')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_catalog(self, **params):
        self.set_method('getCatalog')
        return self.send(params)

    def get_friends_list(self, **params):
        self.set_method('getFriendsList')
        return self.send(params)

    def get_leaderboard(self, **params):
        self.set_method('getLeaderboard')
        return self.send(params)

    def get_score(self, **params):
        self.set_method('getScore')
        return self.send(params)

    def send_request(self, **params):
        self.set_method('sendRequest')
        return self.send(params)

