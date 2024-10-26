from Fifth_Edition_Initiative_Non_Creatures import Fifth_Edition_Initiative_Non_Creatures as Non_Creature

class Fifth_Edition_Legendary_Actions(Non_Creature):
    """ A class representing a D&D 5e Legendary Action. This is a subclass of Fifth_Edition_Initiative_Non_Creatures as 
    it is a Non-Creature that can be added to the initiative order.
    """
    
    def __init__(self, 
                 action_total : int,
                 name : str = "Non_Creature",
                 all_actions: list = [], 
                 description: str = "Default Description"):
        """ A method to be create an instance of the Fifth_Edition_Legendary_Actions class.

        Args:
            action_total (int): An integer representing the maximum number of actions that a Non-Creature can take 
                                before some form of reset, eg. the beginning of a new turn.
            name (str, optional): The Non-Creature's given name. Defaults to "Non_Creature".
            all_actions (list, optional): A list of actions that can be taken once the Non-Creature's 
                                          turn begins. Defaults to [].
            description (str, optional): A description of the Non-Creature. Defaults to "Default Description".
        """
        super.__init__(action_total, 
                       name, all_actions, description)
    
    def __str__(self) -> str:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a str representation.

        Returns:
            str: The str representation of the given object.
        """
        pass 
    
    def should_skip_turn(self) -> bool:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be skipped in the initiative order. 
        True if the given object's turn should be skipped, False otherwise.
        Returns:
            bool: A bool based on whether the given object should be skipped in the initiative order. 
        """
        
        pass 
    
    def should_be_removed_from_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be removed from the initiative order. 
        True if the given object should be removed from the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be removed from the initiative order.
        """
        
        pass
    
    def name(self) -> str:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns the name of the given object in the form of a str.

        Returns:
            str: The name of the given object.
        """
        
        pass
    
    def should_be_added_to_initiative(self) -> bool:
        """ A method inherited from Fifth_Edition_Non_Creatures.
        Returns a bool based on whether the given object should be added to the initiative order.
            True if it should be added to the initiative order, False otherwise.

        Returns:
            bool: A bool based on whether the given object should be added to the initiative order.
        """
        
        pass 
    
    def execute_turn(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes the turn of a Non_Creature.
        """
        
        pass
    
    def beginning_of_turn(self):
        """ A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions necessary for a Non-Creature at the beginning of their turn.
        """
        
        pass 
    
    def long_rest(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions upon a Non-Creature performing a long rest.
        """
        
        pass 
    
    def short_rest(self):
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that executes all actions upon a Non-Creature performing a short rest.
        """
        
        pass 
    
    def description(self) -> str:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns the description of the given object.

        Returns:
            str: The description of the given object.
        """
        pass
    
    def action_total(self) -> int:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns the maximum number of actions that can be take before some form of reset.

        Returns:
            int: The maximum number of actions that can be taken before some form of reset.
        """
        
        pass
    
    def all_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of all actions that a Non-Creature could take.

        Returns:
            list: A list of all actions that a Non-Creature could take.
        """
        
        pass
    
    def currently_available_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of all actions that a Non-Creature can currently take.

        Returns:
            list: A list of all actions that a Non-Creature can currently take.
        """
        
        pass
    
    def taken_actions(self) -> list:
        """A method inherited from Fifth_Edition_Non_Creatures.
        A method that returns a list of actions that have been taken after the last reset.

        Returns:
            list: A list of actions that have been taken after the last reset.
        """
        
        pass 