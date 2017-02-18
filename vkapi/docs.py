from vk import VKAPI


class Docs(VKAPI):
    method_class = 'docs'

    def __init__(self, access_token=''):
        super(Docs, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_types(self, **params):
        self.set_method('getTypes')
        return self.send(params)

    def get_upload_server(self, **params):
        self.set_method('getUploadServer')
        return self.send(params)

    def get_wall_upload_server(self, **params):
        self.set_method('getWallUploadServer')
        return self.send(params)

    def save(self, **params):
        self.set_method('save')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

