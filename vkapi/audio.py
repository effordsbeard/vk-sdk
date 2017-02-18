from vk import VKAPI


class Audio(VKAPI):
    method_class = 'audio'

    def __init__(self, access_token=''):
        super(Audio, self).__init__(access_token=access_token)
    
    def add(self, **params):
        self.set_method('add')
        return self.send(params)

    def add_album(self, **params):
        self.set_method('addAlbum')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def delete_album(self, **params):
        self.set_method('deleteAlbum')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def edit_album(self, **params):
        self.set_method('editAlbum')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_albums(self, **params):
        self.set_method('getAlbums')
        return self.send(params)

    def get_broadcast_list(self, **params):
        self.set_method('getBroadcastList')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_count(self, **params):
        self.set_method('getCount')
        return self.send(params)

    def get_lyrics(self, **params):
        self.set_method('getLyrics')
        return self.send(params)

    def get_popular(self, **params):
        self.set_method('getPopular')
        return self.send(params)

    def get_recommendations(self, **params):
        self.set_method('getRecommendations')
        return self.send(params)

    def get_upload_server(self, **params):
        self.set_method('getUploadServer')
        return self.send(params)

    def move_to_album(self, **params):
        self.set_method('moveToAlbum')
        return self.send(params)

    def reorder(self, **params):
        self.set_method('reorder')
        return self.send(params)

    def restore(self, **params):
        self.set_method('restore')
        return self.send(params)

    def save(self, **params):
        self.set_method('save')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

    def set_broadcast(self, **params):
        self.set_method('setBroadcast')
        return self.send(params)

