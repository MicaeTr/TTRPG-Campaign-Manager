from abc import ABC, abstractmethod

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from Fifth_Edition_Dungeons_And_Dragons.Combat.Fifth_Edition_Initiative_Items import \
    Fifth_Edition_Initiative_Items as Initiative_Items


class Fifth_Edition_Creature(Initiative_Items, ABC):
    """ An abstract class representing all Creature's according to the rules of D&D 5e. It is a subclass of 
    Fifth_Edition_Initiative_Items because a Creature is an item that can be in an initiative order.
    """

    @abstractmethod
    def dex(self) -> int:
        """Returns the dexterity modifier of the given object.

        Returns:
            int: The dexterity modifier of the given object.
        """

        pass

    @abstractmethod
    def new_turn(self):
        """ A method that executes all actions necessary for a Creature at the beginning of their turn.
        """

        pass

    @abstractmethod
    def name(self) -> str:
        """ A method inherited from Fifth_Edition_Initiative_Items.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """

        pass

    @abstractmethod
    def __str__(self) -> str:
        """A method inherited from Fifth_Edition_Initiative_Items.
        Returns a str representation of the given object.

        Returns:
            str: The str representation of the given object.
        """

        pass

    @abstractmethod
    def should_skip_turn(self) -> bool:
        """ A method inherited from Fifth_Edition_Initiative_Items.
        Returns a bool based on whether the given object should be skipped in the initiative order. 
        True if the given object's turn should be skipped, False otherwise.
        Returns:
            bool: A bool based on whether the given object should be skipped in the initiative order. 
        """

        pass

    @abstractmethod
    def should_be_removed_from_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Initiative_Items.
        Returns a bool based on whether the given object should be removed from the initiative order. 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """

        pass
