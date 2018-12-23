from collections import deque

def stableMatching(proposors, acceptors):
    """
        proposors: list of entities that submit proposals
        acceptors: list of entities that consider the proposals from the proposors
    """
    deq = deque(proposors)
    while deq:
        proposor = deq.popleft()
        for preference in proposor.preferences:
            if preference.free:
                proposor.pair = preference
                preference.pair = proposor
                preference.free = False
                proposor.free = False
                break
            elif not preference.free:
                preferencePair = preference.pair
                preferencePairIndex = preference.preferences.index(preference.pair)
                proposorIndex = preference.preferences.index(proposor)
                if proposorIndex < preferencePairIndex:
                    preferencePair.free = True
                    preferencePair.pair = None
                    deq.appendleft(preferencePair)
                    proposor.pair = preference
                    preference.pair = proposor
                    preference.free = False
                    proposor.free = False
                    break
            else:
                raise ValueError("Unexpected status")

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
        self.pair = None

    # Getters and setters are not Pythonic

    def __str__(self):
        return self.name

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
