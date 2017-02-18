from vk import VKAPI


class Groups(VKAPI):
    method_class = 'groups'

    def __init__(self, access_token=''):
        super(Groups, self).__init__(access_token=access_token)
    
    def add_link(self, **params):
        self.set_method('addLink')
        return self.send(params)

    def approve_request(self, **params):
        self.set_method('approveRequest')
        return self.send(params)

    def ban_user(self, **params):
        self.set_method('banUser')
        return self.send(params)

    def create(self, **params):
        self.set_method('create')
        return self.send(params)

    def delete_link(self, **params):
        self.set_method('deleteLink')
        return self.send(params)

    def edit(self, **params):
        self.set_method('edit')
        return self.send(params)

    def edit_link(self, **params):
        self.set_method('editLink')
        return self.send(params)

    def edit_manager(self, **params):
        self.set_method('editManager')
        return self.send(params)

    def edit_place(self, **params):
        self.set_method('editPlace')
        return self.send(params)

    def get(self, **params):
        self.set_method('get')
        return self.send(params)

    def get_banned(self, **params):
        self.set_method('getBanned')
        return self.send(params)

    def get_by_id(self, **params):
        self.set_method('getById')
        return self.send(params)

    def get_callback_confirmation_code(self, **params):
        self.set_method('getCallbackConfirmationCode')
        return self.send(params)

    def get_callback_server_settings(self, **params):
        self.set_method('getCallbackServerSettings')
        return self.send(params)

    def get_callback_settings(self, **params):
        self.set_method('getCallbackSettings')
        return self.send(params)

    def get_catalog(self, **params):
        self.set_method('getCatalog')
        return self.send(params)

    def get_catalog_info(self, **params):
        self.set_method('getCatalogInfo')
        return self.send(params)

    def get_invited_users(self, **params):
        self.set_method('getInvitedUsers')
        return self.send(params)

    def get_invites(self, **params):
        self.set_method('getInvites')
        return self.send(params)

    def get_members(self, **params):
        self.set_method('getMembers')
        return self.send(params)

    def get_requests(self, **params):
        self.set_method('getRequests')
        return self.send(params)

    def get_settings(self, **params):
        self.set_method('getSettings')
        return self.send(params)

    def invite(self, **params):
        self.set_method('invite')
        return self.send(params)

    def is_member(self, **params):
        self.set_method('isMember')
        return self.send(params)

    def join(self, **params):
        self.set_method('join')
        return self.send(params)

    def leave(self, **params):
        self.set_method('leave')
        return self.send(params)

    def remove_user(self, **params):
        self.set_method('removeUser')
        return self.send(params)

    def reorder_link(self, **params):
        self.set_method('reorderLink')
        return self.send(params)

    def search(self, **params):
        self.set_method('search')
        return self.send(params)

    def set_callback_server(self, **params):
        self.set_method('setCallbackServer')
        return self.send(params)

    def set_callback_server_settings(self, **params):
        self.set_method('setCallbackServerSettings')
        return self.send(params)

    def set_callback_settings(self, **params):
        self.set_method('setCallbackSettings')
        return self.send(params)

    def unban_user(self, **params):
        self.set_method('unbanUser')
        return self.send(params)

