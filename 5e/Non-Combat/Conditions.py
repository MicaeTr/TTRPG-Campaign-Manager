import sys 
sys.path.insert(1, 'TTRPG-Campaign-Manager/5e')
from Utils import Condition_Names
"""A class that represents a condition in the game
"""
class Condition:
    def __init__(self, name:Condition_Names, currently_have :bool = False, source:str ="", duration:int=0) -> None:
        self.name = name
        self.currently_have = currently_have
        self.source = source
        self.duration = duration
        
    def gain_condition(self, source, duration):
        self.source = source
        self.duration = duration
        self.currently_have = True
    
    def loose_condition(self):
        self.currently_have = False
        self.source = "" 
        self.duration = 0
    
""" A class that represents the Unconscious condition"""
class Unconscious_Condition(Condition):
    def __init__(self, name: Condition_Names, currently_have: bool = False, successes :int = 0, 
                 failures : int = 0, source: str = "", duration: int = 0) -> None:
        super().__init__(name, currently_have, source, duration)
        self.successes = successes
        self.failures = failures
    
    def fail(self):
        self.failures +=1 
    
    def success(self):
        self.successes +=1

class Exhausted_Condition(Condition):
    def __init__(self, name: Condition_Names, level:int = 0, currently_have: bool = False, source: str = "", duration: int = 0) -> None:
        super().__init__(name, currently_have, source, duration)
        self.level = level
    
    def gain_a_level(self):
        self.level +=1

""" 
    A class that represents all of the conditions that a player may have in the game
"""
class Conditions:
    def __init__(self) -> None:
        self.blinded = Condition(Condition_Names.BLINDED)
        self.charmed = Condition(Condition_Names.CHARMED)
        self.deafened = Condition(Condition_Names.DEAFENED)
        self.frightened = Condition(Condition_Names.FRIGHTENED)
        self.grappled = Condition(Condition_Names.GRAPPLED)
        self.incapacitated = Condition(Condition_Names.INCAPACITATED)
        self.invisible = Condition(Condition_Names.INVISIBLE)
        self.paralyzed = Condition(Condition_Names.PARALYZED)
        self.petrified = Condition(Condition_Names.PETRIFIED)
        self.poisoned = Condition(Condition_Names.POISONED)
        self.prone = Condition(Condition_Names.PRONE)
        self.restrained = Condition(Condition_Names.RESTRAINED)
        self.stunned = Condition(Condition_Names.STUNNED)
        self.concentration = Condition(Condition_Names.CONCENTRATION)
        self.unconscious = Unconscious_Condition(Condition_Names.UNCONSCIOUS)
        self.exhaustion = Exhausted_Condition(Condition_Names.EXHAUSTED)
        
    """Signature: Conditions, Condition_Names -> Str
        Purpose:This function returns a string describing the condition based on the given Condition_Names
        """
    def condition_meanings(self, condition:Condition_Names):
        pass 
    
    def gain_condition(self, condition_name :Condition_Names, source, duration):
        if condition_name == Condition_Names.BLINDED:
            self.blinded.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CHARMED:
            self.charmed.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.DEAFENED:
            self.deafened.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.FRIGHTENED:
            self.frightened.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.GRAPPLED:
            self.grappled.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INCAPACITATED:
            self.incapacitated.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INVISIBLE:
            self.invisible.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PARALYZED:
            self.paralyzed.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PETRIFIED:
            self.petrified.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.POISONED:
            self.poisoned.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PRONE:
            self.prone.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.RESTRAINED:
            self.restrained.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.STUNNED:
            self.stunned.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CONCENTRATION:
            self.concentration.gain_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.UNCONSCIOUS:
            self.unconscious.gain_condition(source=source, duration=duration)
    
    def loose_condition(self, condition_name :Condition_Names, source, duration):
        if condition_name == Condition_Names.BLINDED:
            self.blinded.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CHARMED:
            self.charmed.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.DEAFENED:
            self.deafened.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.FRIGHTENED:
            self.frightened.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.GRAPPLED:
            self.grappled.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INCAPACITATED:
            self.incapacitated.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INVISIBLE:
            self.invisible.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PARALYZED:
            self.paralyzed.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PETRIFIED:
            self.petrified.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.POISONED:
            self.poisoned.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PRONE:
            self.prone.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.RESTRAINED:
            self.restrained.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.STUNNED:
            self.stunned.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CONCENTRATION:
            self.concentration.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.UNCONSCIOUS:
            self.unconscious.loose_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.EXHAUSTED:
            self.exhaustion.loose_condition(source=source, duration=duration)
            self.exhaustion.level = 0
        