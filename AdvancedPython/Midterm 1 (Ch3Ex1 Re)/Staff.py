from Person import Person


class Staff(Person):
    def __init__(self):
        order = {}

    def Tax(self, total):
        return round(0.09 * total, 2)
