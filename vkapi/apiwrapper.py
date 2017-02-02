from newsfeed import Newsfeed

class API(object):

    def __init__(self, access_token=''):
        self.Newsfeed = Newsfeed(access_token=access_token)
