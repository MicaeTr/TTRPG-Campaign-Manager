import sys 
sys.path.insert(1, 'TTRPG-Campaign-Manager/5e')
from Fifth_Edition_Dungeons_And_Dragons.Utils.Utils import Condition_Names

class Condition:
    """A class that represents a D&D 5e Condition. Conditions can be gained during combat but can be gained outside of
    combat as well.
    """
    def __init__(self, name:Condition_Names, currently_have :bool = False, source:str ="", duration:int=0) -> None:
        """A method to create an instance of the Condition class.

        Args:
            name (Condition_Names): The name of the condition
            currently_have (bool, optional): A bool to represent whether a Creature currently
                has a condition. A True value denotes that they have the condition, a False 
                value denotes otherwise. Defaults to False.
            source (str, optional): The source of the condition, eg if it came from a spell or an 
                area of effect. Defaults to "".
            duration (int, optional): The maximum duration of a condition, given in rounds. Defaults to 0.
        """
        self.name = name
        self.currently_have = currently_have
        self.source = source
        self.duration = duration
        
    
    def __str__(self) -> str:
        """Returns a str representation.

        Returns:
            str: The str representation of the given object.
        """
        if self.currently_have:
            return f"\t \t CURRENTLY HAVE - {self.name.upper()} | {self.currently_have} | {self.source} | {self.duration}"
        else:
            return f"\t \t IS NOT {self.name}"
    
    def gain_condition(self, source: str, duration: int):
        """A method that adds all additional details once a condition is gained by a Creature.

        Args:
            source (str): The source of the condition, eg if it came from a spell or an 
                area of effect.
            duration (int): The maximum duration of a condition, given in rounds.
        """
        self.source = source
        self.duration = duration
        self.currently_have = True
    
    def remove_condition(self):
        """A method that removes a condition from a Creature.
        """
        self.currently_have = False
        self.source = "" 
        self.duration = 0
    
class Unconscious_Condition(Condition):
    """ A class that represents the Unconscious condition."""
    def __init__(self, currently_have: bool = False, successes :int = 0, 
                 failures : int = 0, source: str = "", duration: int = 0):
        """A method to create an instance of the Unconscious_Condition class. 

        Args:
            currently_have (bool, optional): A bool to represent whether a Creature currently
                has a condition. A True value denotes that they have the condition, a False 
                value denotes otherwise. Defaults to False.
            successes (int, optional): An int representing the number of Death Save successes a 
                Creature has. Defaults to 0.
            failures (int, optional): An int representing the number. Defaults to 0.
            source (str, optional): The source of the condition, eg if it came from a spell or an 
                area of effect. Defaults to "".
            duration (int, optional): The maximum duration of a condition, given in rounds. Defaults to 0.
        """
        super().__init__(Condition_Names.UNCONSCIOUS, currently_have, source, duration)
        self.successes = successes
        self.failures = failures
    
    def fail(self):
        """A method that performs the actions necessary when a Creature receives a death saving throw failure.
        """
        self.failures +=1 
    
    def success(self):
        """A method that performs the actions necessary when a Creature receives a death saving throw success.
        """
        self.successes +=1
    
    def remove_condition(self):
        """A method that removes the Unconscious_Condition from a Creature.
        """
        self.successes = 0
        self.failures = 0 
        super().remove_condition(self) 

class Exhausted_Condition(Condition):
    """A class representing the Exhausted Condition in accordance to the D&D 5e rules.
    """
    def __init__(self, level:int = 0, 
                 currently_have: bool = False, source: str = "", duration: int = 0) -> None:
        """A method to create an instance of the Exhausted_Condition class.

        Args:
            level (int, optional): An int representing the level of exhaustion. Defaults to 0.
            currently_have (bool, optional): A bool to represent whether a Creature currently
                has a condition. A True value denotes that they have the condition, a False 
                value denotes otherwise. Defaults to False.
            source (str, optional): The source of the condition, eg if it came from a spell or an 
                area of effect. Defaults to "".
            duration (int, optional): The maximum duration of a condition, given in rounds. Defaults to 0.
        """
        super().__init__(Condition_Names.EXHAUSTED, currently_have, source, duration)
        self.level = level
    
    def gain_a_level(self):
        """A method that performs the actions necessary when a Creature gains a level of exhaustion.
        """
        self.level +=1
        
    def remove_condition(self):
        """ A method that performs the actions necessary when a Creature removes a level of exhaustion.
        """
        self.level = 0
        super().remove_condition(self)


class Conditions:
    """
    A class that represents all of the conditions that a player may have in the game
    """
    
    def __init__(self):
        """A method to create an instance of the Conditions class.
        """
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

    def condition_meanings(self, condition:Condition_Names) -> str:
        """This method returns a str describing the condition based on the given Condition_Names.

        Args:
            condition (Condition_Names): The given Condition_Names

        Returns:
            str: The description of the given Condition_Names
        """
        pass 
    
    def gain_condition(self, condition_name :Condition_Names, source, duration):
        """This method performs all actions related to a Creature gaining a Condition based on the given 
        Condition_Names.
        Args:
            condition_name (Condition_Names): The name of the condition being gained.
            source (_type_): The source of the condition, eg if it came from a spell or an 
                area of effect. 
            duration (_type_): The maximum duration of a condition, given in rounds.
        """
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
    
    def remove_condition(self, condition_name :Condition_Names, source, duration):
        """This method performs all actions related to a Creature removing a Condition based on the given 
        Condition_Names.
        
        Args:
            condition_name (Condition_Names): The name of the condition being gained.
            source (_type_): The source of the condition, eg if it came from a spell or an 
                area of effect. 
            duration (_type_): The maximum duration of a condition, given in rounds.
        """
        if condition_name == Condition_Names.BLINDED:
            self.blinded.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CHARMED:
            self.charmed.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.DEAFENED:
            self.deafened.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.FRIGHTENED:
            self.frightened.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.GRAPPLED:
            self.grappled.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INCAPACITATED:
            self.incapacitated.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.INVISIBLE:
            self.invisible.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PARALYZED:
            self.paralyzed.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PETRIFIED:
            self.petrified.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.POISONED:
            self.poisoned.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.PRONE:
            self.prone.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.RESTRAINED:
            self.restrained.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.STUNNED:
            self.stunned.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.CONCENTRATION:
            self.concentration.remove_condition(source=source, duration=duration)
        elif condition_name == Condition_Names.UNCONSCIOUS:
            self.unconscious.remove_condition(source=source, duration=duration)
            
        elif condition_name == Condition_Names.EXHAUSTED:
            self.exhaustion.remove_condition(source=source, duration=duration)
            self.exhaustion.level = 0