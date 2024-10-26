from ..Non_Combat.Conditions import Conditions
from ..Utils.Utils import Condition_Names
from ..Combat.Fifth_Edition_Creature import Fifth_Edition_Creature

class Fifth_Edition_Player(Fifth_Edition_Creature):
    """ A class containing all of the methods necessary for a D&D 5e player. It is a subclass of 
    Fifth_edition_Creature because players are creatures.
    """
    
    def __init__(self, fifth_class : str, name : str, level : int, dex: int):
        """A method to create an instance of the Player class.

        Args:
            fifth_class (str): A str representation of the class of the player.
            name (str): A str of the name of the player.
            level (int): An int to represent the level of the player.
            dex (int): An int to represent the dex modifier of a player.
        """
        self._fifth_class = fifth_class 
        self._name = name
        self._level = level
        self._conditions = Conditions()
        self._dex = dex
    
    def name(self) -> str:
        """A method inherited from Fifth_Edition_Creature.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """
        return self._name
    
    def new_turn(self):
        """ A method inherited from Fifth_Edition_Creature.
        A method that executes all actions necessary for a Creature at the beginning of their turn.
        """
        pass 
    
    def should_skip_turn(self) -> bool:
        """ A method inherited from Fifth_Edition_Creature.
        Returns a bool based on whether the given object should be skipped in the initiative order. 
        True if the given object's turn should be skipped, False otherwise.
        Returns:
            bool: A bool based on whether the given object should be skipped in the initiative order. 
        """
        pass 
    
    def should_be_removed_from_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Creature.
        Returns a bool based on whether the given object should be removed from the initiative order. 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """
        pass
    
    def __str__(self):
        """A method inherited from Fifth_Edition_Creature.
        Returns a str representation of the given object.

        Returns:
            str: The str representation of the given object.
        """
        return f"{self.name} | {self._fifth_class} | {self._level} | {self._conditions} | {self._dex}"
        
    def gain_condition(self,condition_name: Condition_Names, source: str, duration: int):
        """A method for the player to gain a Condition based on the given Condition_Names

        Args:
            condition_name (Condition_Names): The given Condition_Names
            source (str): The source of the Condition.
            duration (int): The maximum duration of the condition given in number of rounds.
        """
        if condition_name == Condition_Names.EXHAUSTED:
            self._conditions.exhaustion.gain_condition()
            self._conditions.exhaustion.gain_a_level()
        else:
            self._conditions.gain_condition(condition_name=condition_name, source=source, duration= duration)
    
    def remove_condition(self, condition_name: Condition_Names):
        """A method for the player to remove a Condition based on the given Condition_Names

        Args:
            condition_name (Condition_Names): The given Condition_Names
        """
        self._conditions.remove_condition(condition_name=condition_name)
            
    def death_saving_throw(self, did_it_succeed: bool):
        """A method for a Player to gain a success or failure from a death saving throw.

        Args:
            did_it_succeed (bool): A bool to represent whether a death saving throw succeeded or failed. 
                A True value denotes a success, a False value denotes a failure.
        """
        if did_it_succeed:
            self._conditions.unconscious.success()
        else:
            self._conditions.unconscious.fail()
    
    def increase_exhaustion(self):
        """A method for a Player to increase their exhaustion level by one.
        """
        self._conditions.exhaustion.gain_a_level()
        
    def dex(self):
        """A method inherited from Fifth_Edition_Creature.
        Returns the dexterity modifier of the given object.

        Returns:
            int: The dexterity modifier of the given object.
        """
        return self._dex
