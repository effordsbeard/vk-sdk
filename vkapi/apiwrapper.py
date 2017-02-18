from account import Account
from apps import Apps
from audio import Audio
from auth import Auth
from board import Board
from database import Database
from docs import Docs
from other import Other
from fave import Fave
from friends import Friends
from gifts import Gifts
from groups import Groups
from likes import Likes
from market import Market
from messages import Messages
from newsfeed import Newsfeed
from notes import Notes
from notifications import Notifications
from pages import Pages
from photos import Photos
from places import Places
from polls import Polls
from search import Search
from stats import Stats
from status import Status
from storage import Storage
from users import Users
from utils import Utils
from video import Video
from wall import Wall
from widgets import Widgets

class API(object):

    def __init__(self, access_token=''):
        self.Account = Account(access_token=access_token)
        self.Apps = Apps(access_token=access_token)
        self.Audio = Audio(access_token=access_token)
        self.Auth = Auth(access_token=access_token)
        self.Board = Board(access_token=access_token)
        self.Database = Database(access_token=access_token)
        self.Docs = Docs(access_token=access_token)
        self.Other = Other(access_token=access_token)
        self.Fave = Fave(access_token=access_token)
        self.Friends = Friends(access_token=access_token)
        self.Gifts = Gifts(access_token=access_token)
        self.Groups = Groups(access_token=access_token)
        self.Likes = Likes(access_token=access_token)
        self.Market = Market(access_token=access_token)
        self.Messages = Messages(access_token=access_token)
        self.Newsfeed = Newsfeed(access_token=access_token)
        self.Notes = Notes(access_token=access_token)
        self.Notifications = Notifications(access_token=access_token)
        self.Pages = Pages(access_token=access_token)
        self.Photos = Photos(access_token=access_token)
        self.Places = Places(access_token=access_token)
        self.Polls = Polls(access_token=access_token)
        self.Search = Search(access_token=access_token)
        self.Stats = Stats(access_token=access_token)
        self.Status = Status(access_token=access_token)
        self.Storage = Storage(access_token=access_token)
        self.Users = Users(access_token=access_token)
        self.Utils = Utils(access_token=access_token)
        self.Video = Video(access_token=access_token)
        self.Wall = Wall(access_token=access_token)
        self.Widgets = Widgets(access_token=access_token)

