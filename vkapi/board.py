from vk import VKAPI


class Board(VKAPI):
    method_class = 'board'

    def __init__(self, access_token=''):
        super(Board, self).__init__(access_token=access_token)
    
    def add_topic(self, **params):
        self.set_method('addTopic')
        return self.send(params)

    def close_topic(self, **params):
        self.set_method('closeTopic')
        return self.send(params)

    def create_comment(self, **params):
        self.set_method('createComment')
        return self.send(params)

    def delete_comment(self, **params):
        self.set_method('deleteComment')
        return self.send(params)

    def delete_topic(self, **params):
        self.set_method('deleteTopic')
        return self.send(params)

    def edit_comment(self, **params):
        self.set_method('editComment')
        return self.send(params)

    def edit_topic(self, **params):
        self.set_method('editTopic')
        return self.send(params)

    def fix_topic(self, **params):
        self.set_method('fixTopic')
        return self.send(params)

    def get_comments(self, **params):
        self.set_method('getComments')
        return self.send(params)

    def get_topics(self, **params):
        self.set_method('getTopics')
        return self.send(params)

    def open_topic(self, **params):
        self.set_method('openTopic')
        return self.send(params)

    def restore_comment(self, **params):
        self.set_method('restoreComment')
        return self.send(params)

    def unfix_topic(self, **params):
        self.set_method('unfixTopic')
        return self.send(params)

