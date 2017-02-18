from vk import VKAPI


class Notes(VKAPI):
    method_class = 'notes'

    def __init__(self, access_token=''):
        super(Notes, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def create_comment(self, **params):
        self.set_method('createComment')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def delete_comment(self, **params):
        self.set_method('deleteComment')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def edit_comment(self, **params):
        self.set_method('editComment')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def restore_comment(self, **params):
        self.set_method('restoreComment')
        return self.send(params)

