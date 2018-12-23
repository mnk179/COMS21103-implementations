def stableMatching(proposers, proposees):
    """
        proposers: list of entities that submit proposals
        proposees: list of entities that consider the proposals from the proposers
    """
    for proposer in proposers:
        pass


class Match(object):
    """
        name: string
        free: boolean
        preferences: list of Match objects, in order of preference
    """
    def __init__(self, name):
        self.name = name
        self.free = True
        self._preferences = []

    # Getters and setters are not Pythonic

    def __str__(self):
        return "A Match object with name " + self.name

    def __repr__(self):
        return self.__str__()

    @property
    def preferences(self):
        return self._preferences

    @preferences.setter
    def preferences(self, values):
        if not all(isinstance(value, Match) for value in values):
            raise TypeError("Preferences must be of type Match")
        else:
            self._preferences = values
