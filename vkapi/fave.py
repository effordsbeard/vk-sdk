from vk import VKAPI


class Fave(VKAPI):
    method_class = 'fave'

    def __init__(self, access_token=''):
        super(Fave, self).__init__(access_token=access_token)
    
    def add_group(self, **params):
        self.set_method('addGroup')
        return self.send(params)

    def add_link(self, **params):
        self.set_method('addLink')
        return self.send(params)

    def add_user(self, **params):
        self.set_method('addUser')
        return self.send(params)

    def get_links(self, **params):
        self.set_method('getLinks')
        return self.send(params)

    def get_market_items(self, **params):
        self.set_method('getMarketItems')
        return self.send(params)

    def get_photos(self, **params):
        self.set_method('getPhotos')
        return self.send(params)

    def get_posts(self, **params):
        self.set_method('getPosts')
        return self.send(params)

    def get_users(self, **params):
        self.set_method('getUsers')
        return self.send(params)

    def get_videos(self, **params):
        self.set_method('getVideos')
        return self.send(params)

    def remove_group(self, **params):
        self.set_method('removeGroup')
        return self.send(params)

    def remove_link(self, **params):
        self.set_method('removeLink')
        return self.send(params)

    def remove_user(self, **params):
        self.set_method('removeUser')
        return self.send(params)

