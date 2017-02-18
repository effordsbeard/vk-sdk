from vk import VKAPI


class Photos(VKAPI):
    method_class = 'photos'

    def __init__(self, access_token=''):
        super(Photos, self).__init__(access_token=access_token)
    
    def confirm_tag(self, **params):
        self.set_method('confirmTag')
        return self.send(params)

    def copy(self, **params):
        self.set_method('copy')
        return self.send(params)

    def create_album(self, **params):
        self.set_method('createAlbum')
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

    def get_albums(self, **params):
        self.set_method('getAlbums')
        return self.send(params)

    def get_albums_count(self, **params):
        self.set_method('getAlbumsCount')
        return self.send(params)

    def get_all(self, **params):
        self.set_method('getAll')
        return self.send(params)

    def get_all_comments(self, **params):
        self.set_method('getAllComments')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_chat_upload_server(self, **params):
        self.set_method('getChatUploadServer')
        return self.send(params)

    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def get_market_album_upload_server(self, **params):
        self.set_method('getMarketAlbumUploadServer')
        return self.send(params)

    def get_market_upload_server(self, **params):
        self.set_method('getMarketUploadServer')
        return self.send(params)

    def get_messages_upload_server(self, **params):
        self.set_method('getMessagesUploadServer')
        return self.send(params)

    def get_new_tags(self, **params):
        self.set_method('getNewTags')
        return self.send(params)

    def get_owner_photo_upload_server(self, **params):
        self.set_method('getOwnerPhotoUploadServer')
        return self.send(params)

    def get_tags(self, **params):
        self.set_method('getTags')
        return self.send(params)

    def get_upload_server(self, **params):
        self.set_method('getUploadServer')
        return self.send(params)

    def get_user_photos(self, **params):
        self.set_method('getUserPhotos')
        return self.send(params)

    def get_wall_upload_server(self, **params):
        self.set_method('getWallUploadServer')
        return self.send(params)

    def make_cover(self, **params):
        self.set_method('makeCover')
        return self.send(params)

    def move(self, **params):
        self.set_method('move')
        return self.send(params)

    def put_tag(self, **params):
        self.set_method('putTag')
        return self.send(params)

    def remove_tag(self, **params):
        self.set_method('removeTag')
        return self.send(params)

    def reorder_albums(self, **params):
        self.set_method('reorderAlbums')
        return self.send(params)

    def reorder_photos(self, **params):
        self.set_method('reorderPhotos')
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

    def save_market_album_photo(self, **params):
        self.set_method('saveMarketAlbumPhoto')
        return self.send(params)

    def save_market_photo(self, **params):
        self.set_method('saveMarketPhoto')
        return self.send(params)

    def save_messages_photo(self, **params):
        self.set_method('saveMessagesPhoto')
        return self.send(params)

    def save_owner_photo(self, **params):
        self.set_method('saveOwnerPhoto')
        return self.send(params)

    def save_wall_photo(self, **params):
        self.set_method('saveWallPhoto')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

