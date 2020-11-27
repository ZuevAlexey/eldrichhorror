class Contact(object):
    def __init__(self, step, test, is_complex=False):
        super().__init__()
        self.step = step
        self.test = test
        self.is_complex = is_complex

    def has_test(self):
        return self.test is None
