from vk import VKAPI


class Wall(VKAPI):
    method_class = 'wall'

    def __init__(self, access_token=''):
        super(Wall, self).__init__(access_token=access_token)
    
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

    def get_reposts(self, **params):
        self.set_method('getReposts')
        return self.send(params)

    def pin(self, **params):
        self.set_method('pin')
        return self.send(params)

    def post(self, **params):
        self.set_method('post')
        return self.send(params)

    def report_comment(self, **params):
        self.set_method('reportComment')
        return self.send(params)

    def report_post(self, **params):
        self.set_method('reportPost')
        return self.send(params)

    def repost(self, **params):
        self.set_method('repost')
        return self.send(params)

    def restore(self, **params):
        self.set_method('restore')
        return self.send(params)

    def restore_comment(self, **params):
        self.set_method('restoreComment')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

    def unpin(self, **params):
        self.set_method('unpin')
        return self.send(params)

