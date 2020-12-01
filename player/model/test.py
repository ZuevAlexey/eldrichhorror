class Test(object):
    def __init__(self, type, modificator, success, fail):
        super().__init__()
        self.type = type
        self.modificator = modificator
        self.success = success
        self.fail = fail

    def has_modificator(self):
        return self.modificator is not None

    def has_success(self):
        return self.success is not None

    def has_fail(self):
        return self.fail is not None

