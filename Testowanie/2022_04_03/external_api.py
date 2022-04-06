class ExternalAPI:
    @classmethod
    def get_data(self):
        with open('a.txt') as f:
            return f.readlines()


def get_only_numbers():
    data = ExternalAPI.get_data()
    result = []
    for line in data:
        if line.isdigit():
            result.append(line)
    return result
