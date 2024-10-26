from Fifth_Edition_Creature import Fifth_Edition_Creature as Creature
from Fifth_Edition_Legendary_Actions import \
    Fifth_Edition_Legendary_Actions as Legendary_Actions


class Fifth_Edition_Monster(Creature):
    """A class representing a D&D 5e Monster. It is a subclass of Fifth_Edition_Creature as it is a Creature that can be 
    added to the initiative order. 
    """

    def __init__(self, legendary_actions: Legendary_Actions = None,
            dex=0) -> None:
        """A method to create an instance of the Fifth_Edition_Monster class.

        Args:
            legendary_actions (Legendary_Actions, optional): Legendary Actions that can be used by 
                a Monster.. Defaults to None.
            dex (int, optional): The dexterity modifier of the Monster. Defaults to 0.
        """
        self.legendary_actions = legendary_actions
        self._dex = 0

    def dex(self) -> int:
        """A method inherited from Fifth_Edition_Creature.
        Returns the dexterity modifier of the given object.

        Returns:
            int: The dexterity modifier of the given object.
        """

        pass

    def new_turn(self):
        """ A method inherited from Fifth_Edition_Creature.
        A method that executes all actions necessary for a Creature at the beginning of their turn.
        """

        pass

    def name(self) -> str:
        """A method inherited from Fifth_Edition_Creature.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """

        pass

    def __str__(self) -> str:
        """A method inherited from Fifth_Edition_Creature.
        Returns a str representation of the given object.

        Returns:
            str: The str representation of the given object.
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
