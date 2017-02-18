from vk import VKAPI


class Video(VKAPI):
    method_class = 'video'

    def __init__(self, access_token=''):
        super(Video, self).__init__(access_token=access_token)
    
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

    def get_albums_by_video(self, **params):
        self.set_method('getAlbumsByVideo')
        return self.send(params)

    def get_catalog(self, **params):
        self.set_method('getCatalog')
        return self.send(params)

    def get_catalog_section(self, **params):
        self.set_method('getCatalogSection')
        return self.send(params)

    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def hide_catalog_section(self, **params):
        self.set_method('hideCatalogSection')
        return self.send(params)

    def remove_from_album(self, **params):
        self.set_method('removeFromAlbum')
        return self.send(params)

    def reorder_albums(self, **params):
        self.set_method('reorderAlbums')
        return self.send(params)

    def reorder_videos(self, **params):
        self.set_method('reorderVideos')
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

    def save(self, **params):
        self.set_method('save')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

