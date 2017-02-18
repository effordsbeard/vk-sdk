from vk import VKAPI


class Auth(VKAPI):
    method_class = 'auth'

    def __init__(self, access_token=''):
        super(Auth, self).__init__(access_token=access_token)
    
    def check_phone(self, **params):
        self.set_method('checkPhone')
        return self.send(params)

    def confirm(self, **params):
        self.set_method('confirm')
        return self.send(params)

    def restore(self, **params):
        self.set_method('restore')
        return self.send(params)

    def signup(self, **params):
        self.set_method('signup')
        return self.send(params)

