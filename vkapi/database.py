from vk import VKAPI


class Database(VKAPI):
    method_class = 'database'

    def __init__(self, access_token=''):
        super(Database, self).__init__(access_token=access_token)
    
    def get_chairs(self, **params):
        self.set_method('getChairs')
        return self.send(params)

    def get_cities(self, **params):
        self.set_method('getCities')
        return self.send(params)

    def get_cities_by_id(self, **params):
        self.set_method('getCitiesById')
        return self.send(params)

    def get_countries(self, **params):
        self.set_method('getCountries')
        return self.send(params)

    def get_countries_by_id(self, **params):
        self.set_method('getCountriesById')
        return self.send(params)

    def get_faculties(self, **params):
        self.set_method('getFaculties')
        return self.send(params)

    def get_regions(self, **params):
        self.set_method('getRegions')
        return self.send(params)

    def get_school_classes(self, **params):
        self.set_method('getSchoolClasses')
        return self.send(params)

    def get_schools(self, **params):
        self.set_method('getSchools')
        return self.send(params)

    def get_streets_by_id(self, **params):
        self.set_method('getStreetsById')
        return self.send(params)

    def get_universities(self, **params):
        self.set_method('getUniversities')
        return self.send(params)

