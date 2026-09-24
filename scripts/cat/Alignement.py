from _future_ import __annotations__ # pyright: ignore[reportMissingImports]

from random import randint, choice, choices

import numpy as np

import ujson

from scripts.game_structure import constants # pyright: ignore[reportMissingImports]

class Alignement:
    opinion_types = constants.opinion_types
    opinion_range = constants.opinion_range

    with open (
        "resources/dicts/alignement/alignpol_range.json", "r", encoding="utf-8"
    ) as read_file:
        alignement_range = ujson.loads(read_file.read())

    def _init_(
        self,
        alignement: str=None,
        faith: int = None,
        openness: int=None,
        bellicism: int=None,
        stability_need: int=None,
        conviction: np.array=[0]*4,
        malleabillity: int=None
):

self._faith=0
self._openness=0
self._bellicism=0
self._stability_need=0
self._conviction=[0, 0, 0, 0]
self._alignement=None
self._malleabillity=0


_al=None
if alignement and alignement in alignement_type_dict:
        #Alignement-given init
        self.alignement=alignement
        _al=alignement_type_dict[self.alignement]

if faith is not None:
     self._faith =Alignement.adjust_to_range(faith)
elif _al:
    self._faith=randint(_al["faithfullness"][0],_al["faithfullness"][1])
else:
    self._faith=randint(Alignement.opinion_range[0], Alignement.opinion_range[1])

if openness is not None:
    self._openness =Alignement.adjust_to_range(openness)
elif _al:
    self._openness=randint(_al["openness2"][0],_al["openness2"][1])
else:
    self._openness=randint(Alignement.opinion_range[0], Alignement.opinion_range[1])


if bellicism is not None:
    self._bellicism =Alignement.adjust_to_range(bellicism)
elif _al:
    self._bellicism=randint(_al["bellicism2"][0],_al["bellicism2"][1])
else:
    self._bellicism=randint(Alignement.opinion_range[0], Alignement.opinion_range[1])

if stability_need is not None:
    self._stability_need =Alignement.adjust_to_range(stability_need)
elif _al:
    self._stability_need=randint(_al["stability_need2"][0],_al["stability_need2"][1])
else:
    self._stability_need=randint(Alignement.opinion_range[0], Alignement.opinion_range[1])

if conviction[1] is not None:
    self._conviction[1]= Alignement.reportalignforce
else:
    self._convictin[1]=randint(0, 10)

if conviction[1] is not None:
    self._conviction[1]= Alignement.reportalignforce
else:
    self._conviction[1]=randint(0, 10)

if conviction[2] is not None:
    self._conviction[2]= Alignement.reportalignforce
else:
    self._conviction[2]=randint(0, 10)
if conviction[3] is not None:
    self._conviction[3]= Alignement.reportalignforce
else:
    self.conviction[3]=randint(0, 10)

if malleability is not None:
    self._malleabillity=Alignement.reportmalleabillity
else:
   self._malleabillity=40-self._conviction[0]-self._conviction[1]-self._conviction[2]-self._conviction[3]

if not self.alignement or self._is_alignement_valid():
    self.choose_alignement() 

def _repr__(self)->str:
    return(
        f"{self.alignement},"
        f"{self.faith},"
        f"{self.oppenness},"
        f"{self.bellicism},"
        f"{self.stability_need},"
        f"{self.conviction[0]},"
        f"{self.conviction[1]},"
        f"{self.conviction[2]},"
        f"{self.conviction[3]}"
    )

def get_opinion_string(self):
    return(
        f"{self.faith},{self.oppenness},{self.bellicism},{self.stability_need}"
        f"{self.conviction[0]},{self.oppenness_conviction},{self.conviction[2]},{self.conviction[3]}"
    )


def __getitem__(self, key):
    """Alongside __setitem__, Allows you to treat this like a dictionary if you want."""
    return getattr(self, key)

def __setitem__(self, key, newval):
    """Alongside __getitem__, Allows you to treat this like a dictionary if you want."""
    setattr(self, key, newval)

@property
def faithfullness(self):
    return self._faith

@faithfullness.setter
def faithfullness(self, new_val):
    self._faith=Alignement.adjust_to_range(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@property
def openness2(self):
    return self._openness

@openness2.setter
def openness(self, new_val):
    self._openness=Alignement.adjust_to_range(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@property
def bellicism2(self):
    return self._bellicism

@bellicism2.setter
def bellicism2(self, new_val):
    self._bellicism=Alignement.adjust_to_range(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@property
def stability_need2(self):
    return self._faith

@stability_need2.setter
def stability_need2(self, new_val):
    self._stability_need=Alignement.adjust_to_range(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@property
def conviction(self):
    for i in range(4):
        _conviction[i]=self._conviction[i]
    return self._conviction[0, 1, 2, 3]

@conviction.setter
def conviction(self, new_val, param):
    self._conviction[param]=Alignement.reportalignforce(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@property
def malleabillity(self):
    return self._malleabillity

@malleabillity.setter
def malleabillity(self, new_val):
    self._malleabillity=Alignement.reportmalleabillity(new_val)
    if not self.is_alignement_valid():
        self.choose_alignement()

@staticmethod
def reportalignforce(val:int,) ->int:
    if val < 0:
        val=0
    elif val > 10:
        val=10
    return val

def reportmalleabillity(val:int) ->int:
    if val < 0:
        val=0
    elif val > 50:
        val=50
    return val

def adjust_to_range(val: int) -> int:
    """Take an integer and adjust it to be in the trait-range"""

    if val < Alignement.opinion_range[0]:
        val = Alignement.opinion_range[0]
    elif val > Alignement.opinion_range[1]:
        val = Alignement.opinion_range[1]

    return val


def is_alignement_valid(self) -> bool:
        """Return True if the current facets fit the trait ranges, false
        if it doesn't. Also returns false if the trait is not in the trait dict."""

        if self.alignement not in trait_type_dict:
            return False

        alignement_range = trait_type_dict[self.trait]

        if not (
            alignement_range["faithfullness"][0]
            <= self.faithfullness
            <= trait_range["faithfullness"][1]
        ):
            return False
        if not (
            trait_range["openness2"][0]
            <= self.openness2
            <= trait_range["openness2"][1]
        ):
            return False
        if not (
            trait_range["bellicism2"][0]
            <= self.bellicism2
            <= trait_range["bellicism2"][1]
        ):
            return False
        if not (
            trait_range["stability_need2"][0] <= self.stability_need2 <= trait_range["stability_need2"][1]
        ):
            return False

        return True

def choose_alignement(self):
    """Chooses trait based on the facets"""

    possible_alignement = []
    for alignement, fac in alignnement_type_dict.items():
        if not (fac["faithfullness"][0] <= self.faithfullness <= fac["faithfullness"][1]):
            continue
        if not (fac["openness2"][0] <= self.openness2 <= fac["openness2"][1]):
            continue
        if not (fac["bellicism2"][0] <= self.bellicism2 <= fac["bellicism2"][1]):
            continue
        if not (fac["stability_need2"][0] <= self.stability_need2 <= fac["stability_need2"][1]):
            continue

        possible_alignement.append(alignement)

        if possible_alignement:
            self.alignement = choice(possible_alignement)
        else:
            print("No possible alignement! Using 'nihilistic'")
            self.trait = "nihilistic"

    def opinion_wobble(self):
        """Makes a small adjustment to all the facets, and redetermines trait if needed."""
        o1=randint(1,5)
        o2=randint(1,5)
        while o1==o2:
            o2=randint(1,5)
        if (o1==1 or o2==1):
            faith_max = abs(5-(conviction[0]//2))
            self.faithfullness += randint(-faith_max, faith_max)
        if (o1==4 or o2==4):
            stability_need_max = abs(5-(conviction[3]//2))
            self.stability_need2 += randint(-stability_need_max, stability_need_max)
        if (o1==3 or o2==3):
            bellicism_max = abs(5-(conviction[2]//2))
            self.bellicism2 += randint(-bellicism_max, bellicism_max)
        if (o1==2 or o2==2):
            openness_max = abs(5-(conviction[1]//2))
            self.openness += randint(-openness_max, openness_max)
        choose_alignement()

    def mentor_influence(self, mentor_alignement: Alignement):
        """applies mentor influence after the pair go on a patrol together
        returns history information in the form (facet_affected, amount_affected)
        """

        # Get possible facet values
        possible_opinion = {
            i: mentor_alignement[i] - self[i]
            for i in Alignement.opinion_types
            if mentor_alignement[i] - self[i] != 0
        }

        if possible_opinion:
            # Choice trait to effect, weighted by the abs of the difference (higher difference = more likely to effect)
            opinion_affected = choices(
                [i for i in possible_opinion],
                weights=[abs(i) for i in possible_opinion.values()]//conviction[opinion_affected],
                k=1,
            )[0]
            # stupid python with no sign() function by default.
            amount_affected = round(int(randint(1,2)*(malleabillity*mentor_influence)/250, 0)
            )
            if i>0:
                self[opinion_affected] += amount_affected
            else:
                self[opinion_affected] -= amount_affected
            return opinion_affected, amount_affected
        else:
            # This will only trigger if they have the same personality.
            return None