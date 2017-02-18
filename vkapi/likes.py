from vk import VKAPI


class Likes(VKAPI):
    method_class = 'likes'

    def __init__(self, access_token=''):
        super(Likes, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def get_list(self, **params):
        self.set_method('getList')
        return self.send(params)

    def is_liked(self, **params):
        self.set_method('isLiked')
        return self.send(params)

