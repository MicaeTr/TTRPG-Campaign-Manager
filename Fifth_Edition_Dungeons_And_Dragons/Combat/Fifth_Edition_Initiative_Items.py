from abc import ABC, abstractmethod


class Fifth_Edition_Initiative_Items(ABC):
    """
    An abstract class that represents any item that can be included in a D&D 5e initiative. 
    """

    @abstractmethod
    def __str__(self) -> str:
        """Returns a str representation.

        Returns:
            str: The str representation of the given object.
        """
        pass

    @abstractmethod
    def should_skip_turn(self) -> bool:
        """ Returns a bool based on whether the given object should be skipped in the initiative order. 
        True if the given object's turn should be skipped, False otherwise.
        Returns:
            bool: A bool based on whether the given object should be skipped in the initiative order. 
        """
        pass

    @abstractmethod
    def should_be_removed_from_initiative(self) -> bool:
        """Returns a bool based on whether the given object should be removed from the initiative order. 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """ Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """
        pass
