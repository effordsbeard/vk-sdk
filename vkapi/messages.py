from vk import VKAPI


class Messages(VKAPI):
    method_class = 'messages'

    def __init__(self, access_token=''):
        super(Messages, self).__init__(access_token=access_token)
    
    def add_chat_user(self, **params):
        self.set_method('addChatUser')
        return self.send(params)

    def allow_messages_from_group(self, **params):
        self.set_method('allowMessagesFromGroup')
        return self.send(params)

    def create_chat(self, **params):
        self.set_method('createChat')
        return self.send(params)

    def delete(self, **params):
        self.set_method('delete')
        return self.send(params)

    def delete_chat_photo(self, **params):
        self.set_method('deleteChatPhoto')
        return self.send(params)

    def delete_dialog(self, **params):
        self.set_method('deleteDialog')
        return self.send(params)

    def deny_messages_from_group(self, **params):
        self.set_method('denyMessagesFromGroup')
        return self.send(params)

    def edit_chat(self, **params):
        self.set_method('editChat')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_chat(self, **params):
        self.set_method('getChat')
        return self.send(params)

    def get_chat_users(self, **params):
        self.set_method('getChatUsers')
        return self.send(params)

    def get_dialogs(self, **params):
        self.set_method('getDialogs')
        return self.send(params)

    def get_history(self, **params):
        self.set_method('getHistory')
        return self.send(params)

    def get_history_attachments(self, **params):
        self.set_method('getHistoryAttachments')
        return self.send(params)

    def get_last_activity(self, **params):
        self.set_method('getLastActivity')
        return self.send(params)

    def get_long_poll_history(self, **params):
        self.set_method('getLongPollHistory')
        return self.send(params)

    def get_long_poll_server(self, **params):
        self.set_method('getLongPollServer')
        return self.send(params)

    def is_messages_from_group_allowed(self, **params):
        self.set_method('isMessagesFromGroupAllowed')
        return self.send(params)

    def mark_as_answered_dialog(self, **params):
        self.set_method('markAsAnsweredDialog')
        return self.send(params)

    def mark_as_important(self, **params):
        self.set_method('markAsImportant')
        return self.send(params)

    def mark_as_important_dialog(self, **params):
        self.set_method('markAsImportantDialog')
        return self.send(params)

    def mark_as_read(self, **params):
        self.set_method('markAsRead')
        return self.send(params)

    def remove_chat_user(self, **params):
        self.set_method('removeChatUser')
        return self.send(params)

    def restore(self, **params):
        self.set_method('restore')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

    def search_dialogs(self, **params):
        self.set_method('searchDialogs')
        return self.send(params)

    def send(self, **params):
        self.set_method('send')
        return self.send(params)

    def set_activity(self, **params):
        self.set_method('setActivity')
        return self.send(params)

    def set_chat_photo(self, **params):
        self.set_method('setChatPhoto')
        return self.send(params)

