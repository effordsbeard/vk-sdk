from vk import VKAPI


class Polls(VKAPI):
    method_class = 'polls'

    def __init__(self, access_token=''):
        super(Polls, self).__init__(access_token=access_token)
    
    def add_vote(self, **params):
        self.set_method('addVote')
        return self.send(params)

    def create(self, **params):
        self.set_method('create')
        return self.send(params)

    def delete_vote(self, **params):
        self.set_method('deleteVote')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_voters(self, **params):
        self.set_method('getVoters')
        return self.send(params)

