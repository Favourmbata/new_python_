class native:
    def __init__(self, name, scv_id):
        self._name = name
        self.scv_id = scv_id

    def get_name(self):
        return self._name


def set_name(self, name):
    self._name = name
