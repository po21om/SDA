
class OdwrotnieClass():
    def __init__(self, name):
        self._name = str(name)

    def reverse(self):
        return ''.join(reversed(self._name))

odwrot = OdwrotnieClass("cosik")
print(odwrot._name)