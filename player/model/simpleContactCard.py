class SimpleContactCard(object):
    def __init__(self, contact_id, version, simpleContacts):
        super().__init__()
        self.id = contact_id
        self.version = version
        self.contacts = simpleContacts

    def get_contact(self, location):
        result = self.simpleContacts[location]
        if result is not None:
            return result

        raise IndexError(f'Card doesn\'t contain a contact in location {location}')

    def get_unique_id(self):
        return str(self.id)
