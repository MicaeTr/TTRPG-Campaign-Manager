from abc import ABC, abstractmethod
from Fifth_Edition_Initiative_Items import \
    Fifth_Edition_Initiative_Items as Initiative_Items


class Fifth_Edition_Initiative_Non_Creatures(ABC, Initiative_Items):
    """
    A class representing items that can be added to a D&D 5e initiative that are not creatures, such as Lair Actions which
    can be dependent or independent from a creature and Legendary Actions which are dependent on a creature
    but are not Creatures themselves. This is an abstract class as a Non-Creature cannot exist as 
    a non-specified non-creature. It is a subclass of Fifth_Edition_Initiative_Items.
    """

    @abstractmethod
    def __init__(self,
            action_total: int,
            name: str = "Non-Creature",
            all_actions: list = [],
            description: str = "Default Description"):
        """ A method to be inherited by subclasses of Non-Creature.

        Args:
            action_total (int): An integer representing the maximum number of actions that a Non-Creature can take 
                                before some form of reset, eg. the beginning of a new turn or a rest.
            name (str, optional): The Non-Creature's given name. Defaults to "Non-Creature".
            all_actions (list, optional): A list of actions that can be taken once the Non-Creature's 
                                          turn begins. Defaults to [].
            description (str, optional): A description of the Non-Creature. Defaults to "Default Description".
        """

        self._action_total = action_total
        self._name = name
        self._all_actions = all_actions
        self._description = description

        self._available_actions = []
        self._taken_actions = []

    @abstractmethod
    def __str__(self) -> str:
        """ A method inherited from Fifth_Edition_Initiative_Items.
        Returns a str representation.

        Returns:
            str: The str representation of the given object.
        """

        returning = f"Name : {self._name} \n\t Number of Actions That Can Be Taken Before Reset:"
        +f" {self._action_total}\n \tAll Actions : {self._all_actions} | Available Actions : {self._available_actions} |"
        + f" Taken Actions : {self._taken_actions}\n\t Description : {self._description} "

        return returning

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
        """A method inherited from Fifth_Edition_Initiative_Items.
        Returns a bool based on whether the given object should be removed from the initiative order. 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """

        pass

    @abstractmethod
    def name(self) -> str:
        """ A method inherited from Fifth_Edition_Initiative_Items.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """

        return self._name

    @abstractmethod
    def should_be_added_to_initiative(self) -> bool:
        """ Returns a bool based on whether the given object should be added to the initiative order.
            True if it should be added to the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be added to the initiative order.
        """

        pass

    @abstractmethod
    def execute_turn(self):
        """A method that executes the turn of a Non_Creature.
        """

        pass

    @abstractmethod
    def beginning_of_turn(self):
        """ A method that executes all actions necessary for a Non-Creature at the beginning of their turn.
        """

        pass

    @abstractmethod
    def long_rest(self):
        """A method that executes all actions upon a Non-Creature performing a long rest.
        """

        pass

    @abstractmethod
    def short_rest(self):
        """A method that executes all actions upon a Non-Creature performing a short rest.
        """

        pass

    @abstractmethod
    def description(self) -> str:
        """A method that returns the description of the given object.

        Returns:
            str: The description of the given object.
        """
        return self._description

    @abstractmethod
    def action_total(self) -> int:
        """A method that returns the maximum number of actions that can be take before some form of reset.

        Returns:
            int: The maximum number of actions that can be taken before some form of reset.
        """

        return self._action_total

    @abstractmethod
    def all_actions(self) -> list:
        """A method that returns a list of all actions that a Non-Creature could take.

        Returns:
            list: A list of all actions that a Non-Creature could take.
        """

        return self._all_actions

    @abstractmethod
    def currently_available_actions(self) -> list:
        """A method that returns a list of all actions that a Non-Creature can currently take.

        Returns:
            list: A list of all actions that a Non-Creature can currently take.
        """

        return self._available_actions

    @abstractmethod
    def taken_actions(self) -> list:
        """A method that returns a list of actions that have been taken after the last reset.

        Returns:
            list: A list of actions that have been taken after the last reset.
        """

        return self._taken_actions
