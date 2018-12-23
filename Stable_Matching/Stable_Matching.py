def stableMatching(proposers, proposees):
    """
        proposers: list of entities that submit proposals
        proposees: list of entities that consider the proposals from the proposers
    """
    pass

class Match(object):
    def __init__(self, name):
        self.name = name
        self.free = True

    # Getters and setters are not Pythonic

    def __str__(self):
        return "A Match object with name " + self.name

    def __repr__(self):
        return self.__str__()
