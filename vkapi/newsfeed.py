from vk import VKAPI


class Newsfeed(VKAPI):
    method_class = 'newsfeed'

    def __init__(self, access_token=''):
        super(Newsfeed, self).__init__(access_token=access_token)

    def add_ban(self, **params):

        self.set_method('addBan')

        return self.send(params)

    def delete_ban(self, **params):

        self.set_method('deleteBan')

        return self.send(params)

    def delete_list(self, **params):

        self.set_method('deleteList')

        return self.send(params)

    def get(self, **params):

        self.set_method('get')

        return self.send(params)

    def get_banned(self, **params):

        self.set_method('getBanned')

        return self.send(params)

    def get_comments(self, **params):

        self.set_method('getComments')

        return self.send(params)

    def get_lists(self, **params):

        self.set_method('getLists')

        return self.send(params)

    def get_mentions(self, **params):

        self.set_method('getMentions')

        return self.send(params)

    def get_recommended(self, **params):

        self.set_method('getRecommended')

        return self.send(params)

    def get_suggested_sources(self, **params):

        self.set_method('getSuggestedSources')

        return self.send(params)

    def ignore_item(self, **params):

        self.set_method('ignoreItem')

        return self.send(params)

    def save_list(self, **params):

        self.set_method('saveList')

        return self.send(params)

    def search(self, **params):

        self.set_method('search')

        return self.send(params)

    def unignore_item(self, **params):

        self.set_method('unignoreItem')

        return self.send(params)

    def unsubscribe(self, **params):

        self.set_method('unsubscribe')

        return self.send(params)

