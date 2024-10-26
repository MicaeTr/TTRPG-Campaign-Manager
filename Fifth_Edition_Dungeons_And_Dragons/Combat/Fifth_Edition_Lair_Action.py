from Fifth_Edition_Initiative_Non_Creatures import \
    Fifth_Edition_Initiative_Non_Creatures as Non_Creature
from Fifth_Edition_Monster import Fifth_Edition_Monster as Monster
import copy


class Fifth_Edition_Lair_Action(Non_Creature):
    """ A class representing a D&D 5e Lair Action. This is a subclass of Fifth_Edition_Initiative_Non_Creatures as 
    it is a Non-Creature that can be added to the initiative order.
    """

    def __init__(self,
            action_total: int = 1,
            name: str = "Lair Actions",
            all_actions: list[str] = [],
            description: str = "A Lair Action",
            monster: Monster = None,
            can_repeat_actions_two_rounds_in_a_row: bool = False,
            can_repeat_actions_only_after_a_rest: bool = False,
            skip_if_monster_is_skipped: bool = False,
            should_be_removed_if_monster_is_removed: bool = False,
            is_first_round_and_is_not_surprised: bool = True):
        """A method to create an instance of the Fifth_Edition_Lair_Action class.

        Args:
            action_total (int, optional): An integer representing the maximum number of actions that a Non-Creature can take 
                                        before some form of reset, eg. the beginning of a new turn.. Defaults to 1.
            name (str, optional): The Non-Creature's given name. Defaults to "Lair Actions".
            all_actions (list[str], optional): A list of actions that can be taken once the Non-Creature's 
                                        turn begins. Defaults to [].
            description (str, optional): A description of the Non-Creature. Defaults to "A Lair Action".
            monster (Monster, optional): The given optional Fifth_Edition_Monster that a Lair Action is 
                                        dependant on. Defaults to None.
            can_repeat_actions_two_rounds_in_a_row (bool, optional): A bool that represents whether a 
                                        Lair Action can repeat the same action two combat
                                        rounds in a row. A True value denotes that this Lair Action 
                                        can repeat the same action two combat rounds in a row, a 
                                        False value denotes that it cannot. Defaults to False.
            can_repeat_actions_only_after_a_rest (bool, optional): A bool that represents whether a 
                                        Lair Action can only repeat actions after a form of rest. 
                                        A True value denotes that this Lair Action can only 
                                        repeat actions after a rest, a False value denotes that 
                                        it can repeat actions even if a rest is not taken. Defaults to False.
            skip_if_monster_is_skipped (bool, optional): A bool that represents whether the Lair Action
                                        can be skipped if the given Monster's turn is also skipped.
                                        A True value denotes that the Lair Action should be skipped if
                                        the given Monster's turn is skipped, a False value denotes 
                                        that the Lair Action should not be skipped. Defaults to False.
            should_be_removed_if_monster_is_removed (bool, optional): A bool that represents whether the 
                                        Lair Action should be removed from the initiative order if the 
                                        given Monster is removed from the initiative order. 
                                        A True value denotes that the Lair Action should be removed, 
                                        a False value denotes that it should not be removed. Defaults to False.
            is_first_round_and_is_not_surprised (bool, optional): A bool that represents whether 
                                        it is the first round of combat and that it is not a surprise round.
                                        A True value denotes that it is the first round of combat and 
                                        that it is not a surprise round, a False value denotes that 
                                        it is not the first round or that it is a surprise round of combat. 
                                        Defaults to True.
        """

        super.__init__(action_total,
                       name, all_actions, description)
        self.__monster = monster
        self.__can_repeat_actions_two_rounds_in_a_row = can_repeat_actions_two_rounds_in_a_row
        self.__can_repeat_actions_only_after_a_rest = can_repeat_actions_only_after_a_rest
        self.__skip_if_monster_is_skipped = skip_if_monster_is_skipped
        self.__should_be_removed_if_monster_is_removed = should_be_removed_if_monster_is_removed
        self.__is_first_round_and_is_not_surprised = is_first_round_and_is_not_surprised
        self.__number_of_actions_taken = 0

    def __str__(self) -> str:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a str representation.

        Returns:
            str: The str representation of the given object.
        """
        super_string = super().__str__()
        super_string = super_string
        + f" Monster : {self.__monster} \n\t"
        +f" Can Repeat Actions Two Rounds in a Row : {self.__can_repeat_actions_two_rounds_in_a_row}\n\t"
        + f" Can Repeat Actions Only After a Rest : {self.__can_repeat_actions_only_after_a_rest}\n\t"
        + f" Skip If Monster Is Skipped : {self.__skip_if_monster_is_skipped} |"
        + f" Should be Removed if Monster is Removed : {self.__should_be_removed_if_monster_is_removed}"
        return super_string

    def should_skip_turn(self) -> bool:
        """A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be skipped in the initiative order. 
        True if the given object's turn should be skipped, False otherwise.
        Returns:
            bool: A bool based on whether the given object should be skipped in the initiative order. 
        """
        if self.__monster is not None and self.__skip_if_monster_is_skipped:
            return self.__monster.should_skip_turn()
        return False

    def should_be_removed_from_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be removed from the initiative order- 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """
        return self.__should_be_removed_if_monster_is_removed and self.__monster.should_be_removed_from_initiative()

    def should_be_added_to_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be added to the initiative order -
        True if it should be added to the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be added to the initiative order.
        """
        return not self.should_be_removed_from_initiative()

    def execute_turn(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes the turn of a Non_Creature.
        """
        pass

    def beginning_of_turn(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions necessary for a Non-Creature at the beginning of their turn.
        """
        self.__number_of_actions_taken = 0
        if self.__can_repeat_actions_two_rounds_in_a_row:
            self._available_actions = copy.deepcopy(self._all_actions)
            self._taken_actions = []
        else:
            current_available_actions = []
            for action in self._all_actions:
                if action not in self._taken_actions:
                    current_available_actions.append(action)
            self._available_actions = current_available_actions

    def long_rest(self):
        """ A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions upon a Non-Creature performing a long rest.
        """
        self.__rest()

    def short_rest(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions upon a Non-Creature performing a short rest.
        """
        self.__rest()

    def __rest(self):
        """A method to centralize the short_rest and long_rest methods as there is no difference between the two 
        for Fifth_Edition_Lair_Actions.
        """
        if self.__can_repeat_actions_only_after_a_rest:
            self._available_actions = copy.deepcopy(self._all_actions)
            self._taken_actions = []

    def description(self) -> str:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns the description of the given object.

        Returns:
            str: The description of the given object.
        """
        super().description()

    def name(self) -> str:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """
        super().name()

    def action_total(self) -> int:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns the maximum number of actions that can be take before some form of reset.

        Returns:
            int: The maximum number of actions that can be taken before some form of reset.
        """
        super().action_total()

    def all_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of all actions that a Non-Creature could take.

        Returns:
            list: A list of all actions that a Non-Creature could take.
        """
        super().all_actions()

    def currently_available_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of all actions that a Non-Creature can currently take.

        Returns:
            list: A list of all actions that a Non-Creature can currently take.
        """
        super().currently_available_actions()

    def taken_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of actions that have been taken after the last reset.

        Returns:
            list: A list of actions that have been taken after the last reset.
        """
        super().taken_actions()
