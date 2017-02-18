from vk import VKAPI


class Account(VKAPI):
    method_class = 'account'

    def __init__(self, access_token=''):
        super(Account, self).__init__(access_token=access_token)
    
    def ban_user(self, **params):
        self.set_method('banUser')
        return self.send(params)

    def change_password(self, **params):
        self.set_method('changePassword')
        return self.send(params)

    def get_active_offers(self, **params):
        self.set_method('getActiveOffers')
        return self.send(params)

    def get_app_permissions(self, **params):
        self.set_method('getAppPermissions')
        return self.send(params)

    def get_banned(self, **params):
        self.set_method('getBanned')
        return self.send(params)

    def get_counters(self, **params):
        self.set_method('getCounters')
        return self.send(params)

    def get_info(self, **params):
        self.set_method('getInfo')
        return self.send(params)

    def get_profile_info(self, **params):
        self.set_method('getProfileInfo')
        return self.send(params)

    def get_push_settings(self, **params):
        self.set_method('getPushSettings')
        return self.send(params)

    def lookup_contacts(self, **params):
        self.set_method('lookupContacts')
        return self.send(params)

    def register_device(self, **params):
        self.set_method('registerDevice')
        return self.send(params)

    def save_profile_info(self, **params):
        self.set_method('saveProfileInfo')
        return self.send(params)

    def set_info(self, **params):
        self.set_method('setInfo')
        return self.send(params)

    def set_name_in_menu(self, **params):
        self.set_method('setNameInMenu')
        return self.send(params)

    def set_offline(self, **params):
        self.set_method('setOffline')
        return self.send(params)

    def set_online(self, **params):
        self.set_method('setOnline')
        return self.send(params)

    def set_push_settings(self, **params):
        self.set_method('setPushSettings')
        return self.send(params)

    def set_silence_mode(self, **params):
        self.set_method('setSilenceMode')
        return self.send(params)

    def unban_user(self, **params):
        self.set_method('unbanUser')
        return self.send(params)

    def unregister_device(self, **params):
        self.set_method('unregisterDevice')
        return self.send(params)

