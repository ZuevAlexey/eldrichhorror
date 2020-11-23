class SimpleContactCard(object):
    def __init__(self, contact_id, version, contacts):
        super().__init__()
        self.id = contact_id
        self.version = version
        self.contacts = contacts

    def get_contact(self, location):
        result = self.contacts[location]
        if result is not None:
            return result

        raise IndexError(f'Card doesn\'t contain a contact in location {location}')
