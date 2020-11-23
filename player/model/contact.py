class Contact(object):
    def __init__(self, step, test):
        super().__init__()
        self.step = step
        self.test = test

    def has_test(self):
        return self.test is None
