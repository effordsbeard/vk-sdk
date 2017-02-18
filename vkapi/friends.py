from vk import VKAPI


class Friends(VKAPI):
    method_class = 'friends'

    def __init__(self, access_token=''):
        super(Friends, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def add_list(self, **params):
        self.set_method('addList')
        return self.send(params)

    def are_friends(self, **params):
        self.set_method('areFriends')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def delete_all_requests(self, **params):
        self.set_method('deleteAllRequests')
        return self.send(params)

    def delete_list(self, **params):
        self.set_method('deleteList')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def edit_list(self, **params):
        self.set_method('editList')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_app_users(self, **params):
        self.set_method('getAppUsers')
        return self.send(params)

    def get_by_phones(self, **params):
        self.set_method('getByPhones')
        return self.send(params)

    def get_lists(self, **params):
        self.set_method('getLists')
        return self.send(params)

    def get_mutual(self, **params):
        self.set_method('getMutual')
        return self.send(params)

    def get_online(self, **params):
        self.set_method('getOnline')
        return self.send(params)

    def get_recent(self, **params):
        self.set_method('getRecent')
        return self.send(params)

    def get_requests(self, **params):
        self.set_method('getRequests')
        return self.send(params)

    def get_suggestions(self, **params):
        self.set_method('getSuggestions')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

