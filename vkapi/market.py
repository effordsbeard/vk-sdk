from vk import VKAPI


class Market(VKAPI):
    method_class = 'market'

    def __init__(self, access_token=''):
        super(Market, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def add_album(self, **params):
        self.set_method('addAlbum')
        return self.send(params)

    def add_to_album(self, **params):
        self.set_method('addToAlbum')
        return self.send(params)

    def create_comment(self, **params):
        self.set_method('createComment')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def delete_album(self, **params):
        self.set_method('deleteAlbum')
        return self.send(params)

    def delete_comment(self, **params):
        self.set_method('deleteComment')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def edit_album(self, **params):
        self.set_method('editAlbum')
        return self.send(params)

    def edit_comment(self, **params):
        self.set_method('editComment')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_album_by_id(self, **params):
        self.set_method('getAlbumById')
        return self.send(params)

    def get_albums(self, **params):
        self.set_method('getAlbums')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_categories(self, **params):
        self.set_method('getCategories')
        return self.send(params)

    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def remove_from_album(self, **params):
        self.set_method('removeFromAlbum')
        return self.send(params)

    def reorder_albums(self, **params):
        self.set_method('reorderAlbums')
        return self.send(params)

    def reorder_items(self, **params):
        self.set_method('reorderItems')
        return self.send(params)

    def report(self, **params):
        self.set_method('report')
        return self.send(params)

    def report_comment(self, **params):
        self.set_method('reportComment')
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

