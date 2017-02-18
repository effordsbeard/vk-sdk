from vk import VKAPI


class Places(VKAPI):
    method_class = 'places'

    def __init__(self, access_token=''):
        super(Places, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def checkin(self, **params):
        self.set_method('checkin')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_checkins(self, **params):
        self.set_method('getCheckins')
        return self.send(params)

    def get_types(self, **params):
        self.set_method('getTypes')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

