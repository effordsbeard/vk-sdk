from vk import VKAPI


class Pages(VKAPI):
    method_class = 'pages'

    def __init__(self, access_token=''):
        super(Pages, self).__init__(access_token=access_token)
    
    def clear_cache(self, **params):
        self.set_method('clearCache')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_history(self, **params):
        self.set_method('getHistory')
        return self.send(params)

    def get_titles(self, **params):
        self.set_method('getTitles')
        return self.send(params)

    def get_version(self, **params):
        self.set_method('getVersion')
        return self.send(params)

    def parse_wiki(self, **params):
        self.set_method('parseWiki')
        return self.send(params)

    def save(self, **params):
        self.set_method('save')
        return self.send(params)

    def save_access(self, **params):
        self.set_method('saveAccess')
        return self.send(params)

