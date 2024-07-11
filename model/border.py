from dataclasses import dataclass

from model.country import Country


@dataclass
class Border:
    _state1no: int
    _state2no: int
    _year: int
    _conttype:int

    @property
    def conttype(self):
        return self._conttype
    @property
    def state2no(self):
        return self._state2no
    @property
    def state1no(self):
        return self._state1no

    @property
    def year(self):
        return self._year

    def __hash__(self):
        return hash(str(self.state1no)+" "+str(self.state2no))

    def __eq__(self, other):
        if self.state1no == other.state1no and self.state2no == other.state2no:
            return True
        else:
            return False

    def __str__(self):
        return f"Border between {str(self.state1no)} and {self.state2no} from {self.year}"