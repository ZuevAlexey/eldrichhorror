class ComplexContactCard(object):
    def __init__(self, contact_id, version, location, contact):
        super().__init__()
        self.id = contact_id
        self.version = version
        self.location = location
        self._contact = contact

    def has_location(self):
        return self.location is not None

    def get_unique_id(self):
        return (self.location.name + '_' if self.location is not None else '') + str(self.id)

    def get_contact(self):
        return self._contact
