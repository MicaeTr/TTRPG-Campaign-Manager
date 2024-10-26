from Fifth_Edition_Dungeons_And_Dragons.Combat.Fifth_Edition_Initiative_Items import Fifth_Edition_Initiative_Items as Initiative_Items


class Fifth_Edition_Initiative:
    """
    This class keeps track of initiative according to D&D 5e rules. In addition to Creatures, 
    this class can also keep track of Lair Actions and Legendary Actions so that GMs do not forget
    actions that are available to them. It can also add or remove additional items in the middle of combat, 
    let GMs manually change the combat order, and sort initiative rolls based on an item's dexterity modifier. 
    """

    def __init__(self, surprise_round: bool = False, sort_on_dex: bool = False):
        """ Initializes initiative - the order in which players take turn in combat.
        Args:
            surprise_round: bool - A bool for whether or not the Initiative starts in a surprise round. A True value denotes
                            that it is starting on a surprise round, a False value denotes otherwise.
            sort_on_dex: bool - A bool for whether Initiative rolls should have ties broken based on a Creature's dex score. 
                        A True value denotes that it is sorted by an item's dexterity modifier, a False value denotes otherwise.
        Fields:
            __sorted_init: list((Initiative_Items, int)) - A sorted version of initiative, with the item with the 
                highest roll at __sorted_init[0]. 
            __current_init: int - The index of the current initiative 
            __surprise_round: bool - A bool to indicate whether there is a surprise round. A True value denotes that it is 
                            a surprise round, a False value denotes otherwise.
            __sort_on_dex: bool - A bool as to indicate whether __sorted_init should take into account a 
                Creature's dex scores when breaking Initiative ties. A True value denotes that the initiative should use
                dexterity modifiers to break initiative ties, a False value denotes otherwise.
        """
        self.__sorted_init = []
        self.__manual_changes = []
        self.__current_init = 0
        self.__surprise_round = surprise_round
        self.__sort_on_dex = sort_on_dex
        
  
    def __str__(self) -> str:
        """Returns a str representation of the Initiative class.

        Returns:
            str: A representation of the Initiative class.
        """
        string_init = " \n"
        for item in self.__sorted_init:
            string_init += f"{item}\n"
        return f"Full Initiative Order:{string_init}\nCurrent Initiative Index: {self.__current_init}, \
            Surprise Round: {self.__surprise_round}, Sort On Dex: {self.__sort_on_dex}"
    
    
    def current_initiative_order(self) -> list[tuple[Initiative_Items, int]]:
        """Returns the current Initiative order as a list of tuple[Initiative_Items, int] where the int represents 
        the initiative of the Initiative_Items. For example, if we are currently on Apollo's initiative, 
        and the initiative order is (Artemis, 25), (Athena, 20), (Apollo, 15), and (Zeus, 10). This will return 
        (Apollo, 15), (Zeus,10), (Artemis, 25), and (Athena, 20).
        Returns:
            list[tuple[Initiative_Items, int]] : The current initiative order as a list of (Initiative_Items, int) 
                where the int represents the rolled initiative of the Creature.
        """        
        index = self.__current_init
        first_iteration = True
        order_as_list = []
        while first_iteration or (index % len(self.__sorted_init)) != self.__current_init:
            adjusted_index = index % len(self.__sorted_init)
            order_as_list.append(self.__sorted_init[adjusted_index])
            index += 1
            if first_iteration:
                first_iteration = False
        return order_as_list
     
    def full_initiative_order(self) -> list[tuple[Initiative_Items, int]]:
        """Returns the full initiative order as a list of tuple[Initiative_Items, int] where the int represents the
        initiative of the Initiative_Items. For example, if we are currently on Apollo's initiative
        and the initiative order is (Artemis, 25), (Athena, 20), (Apollo, 15), and (Zeus, 10) -
        it will return a list of (Artemis, 25), (Athena, 20), (Apollo, 15), and (Zeus, 10)

        Returns:
            list[tuple[Initiative_Items, int]]: The full initiative order as a list of (Initiative_Items, int) 
                where the int represents the initiative of the Initiative_Items.
        """        
        return self.__sorted_init
    
    def current_item(self) -> Initiative_Items:
        """Returns the Initiative_Items whose turn it currently is according to the initiative order.

        Returns:
            Initiative_Items: The Initiative_Items whose turn it currently is according the the initiative order.
        """        
        return self.__sorted_init[self.__current_init]
     
     
    def initial_add(self, additions: list[tuple[Initiative_Items, int]]) -> None :
        """Adds the initial initiative rolls to the object and sorts it according to specifications.

        Args:
            additions: list[(Initiative_Items, int)] : A list of Initiative_Items to be 
                processed and added to self.__sorted_init where the int represents the 
                initiative of the Initiative_Items.
        """        
        additions.sort(reverse=True, key=sort_key_on_roll)
        inits = [x[1] for x in additions]
        if not self.__sort_on_dex or len(inits) == len(set(inits)): 
            self.__sorted_init = additions 
        else : 
            index_dict = {}
            for index, number in enumerate(inits):
                if number in index_dict:
                    index_dict[number].append(index)
                else:
                    index_dict[number] = [index]
                duplicate_inits = [indices for indices in index_dict.values() if len(indices) > 1]
            
            curr_index_additions = 0 
            curr_duplicate_inits_index = 0 
            while curr_index_additions < len(additions):
                
                if curr_duplicate_inits_index < len(duplicate_inits) \
                and curr_index_additions in duplicate_inits[curr_duplicate_inits_index]:
                    
                    curr_duplicate_inits = duplicate_inits[curr_duplicate_inits_index]
                    same_initiative = []
                    for index in curr_duplicate_inits:
                        same_initiative.append(additions[index])
                        curr_index_additions += 1
                    curr_duplicate_inits_index += 1
                    same_initiative.sort(reverse=True, key=lambda x: x[0].dex())
                    self.__sorted_init += same_initiative
                else: 
                    self.__sorted_init.append(additions[curr_index_additions])
                    curr_index_additions += 1
    
    
    def manual_change(self, old_index:int, new_index:int) -> None: 
        """ A function to allow manual changes to the initiative order by the GM. 

        Args:
            old_index (int): The old index of the creature being moved.
            new_index (int): The new index of the creature being moved.
        """        
        creature = self.__sorted_init.pop(old_index)
        self.__manual_changes.append(creature)
        if new_index > len(self.__sorted_init):
            raise IndexError("Fifth_Edition_Initiative line 131 Error - \
                             Manual Change Error- new_index out of bounds of Initiative Order")
        self.__sorted_init.insert(new_index, creature)
        if old_index < self.__current_init and new_index > self.__current_init:
            self.move_backward()
        if new_index < self.__current_init and old_index > self.__current_init:
            self.move_forward()
                
    
    def remove_during_combat(self, removals: list[tuple[Initiative_Items, int]]) -> None: 
        """Removes all given Initiative_Items from self.__sorted_init

        Args:
            removals (list[tuple[Initiative_Items, int]]): A list of all of the Initiative_Items 
                being removed from __sorted_init where the int represented the initiative of the Initiative_Items.
        """        
        for creature in removals:
            self.__singular_remove(creature)
    
    def add_during_combat(self, additions: list[tuple[Initiative_Items, int]]) -> None:
        """Adds multiple Initiative_Items in the middle of combat. 

        Args:
            additions (list[tuple[Initiative_Items, int]]): Initiative_Items to add to __sorted_init where int 
                represents the initiative of the Initiative_Items.
        """        
        for creature in additions:
            self.__singular_add(creature)
        
    
    def __singular_remove(self, removal: tuple[Initiative_Items, int]) -> None: 
        """Removes a single given Initiative_Items from self.__sorted_init in the middle of combat.

        Args:
            removal (tuple[Initiative_Items, int]): The (Initiative_Items, int) that is to be removed 
                from self.__sorted_init where the int represent the initiative of the Initiative_Items.
        """
        index_of_removal = self.__sorted_init.index(removal)
        self.__sorted_init.remove(removal)
        
        if removal in self.__manual_changes:
            self.__manual_changes.remove(removal)
            
        if index_of_removal == self.__current_init == len(self.__sorted_init):
            self.__current_init = 0
        if index_of_removal < self.__current_init:
            self.move_backward()
        
    
    def __singular_add(self, addition: tuple[Initiative_Items, int]) -> None: 
        """Adds a singular given Initiative_Items according to the given initiative roll to 
        self.__sorted_init in the middle of combat.

        Args:
            addition tuple[Initiative_Items,int]: The (Initiative_Items, int) that is to be added from 
                self.__sorted_init where int represented the initiative of the Initiative_Items.
        """

        adding_creature, adding_init = addition 
        pos = 0 
        first_check = True
        for index, (creature, init) in enumerate(self.__sorted_init):
            
            dex_check = adding_init == init and self.__sort_on_dex and adding_creature.dex() >= creature.dex()
            
            if (creature, init) in self.__manual_changes:
                continue
            if adding_init > init:
                pos = index 
                break
            if dex_check and first_check:
                pos = 0 
                break
            if dex_check:
                pos = index + 1 
                break
            pos = index + 1
            first_check =  False
        self.__sorted_init.insert(pos, addition)
        if pos <= self.__current_init:
            self.move_forward()
        
    def __move(self, addition: int) -> None:
        """ Moves __current_init based on the given int.

        Args:
            addition (int): The given int.
        """        
        self.__current_init += addition
        self.__current_init = self.__current_init % len(self.__sorted_init)
        
    def move_forward(self) -> None : 
        """Moves __current_init forward and adjusts self.__surprise_round if the surprise round has ended.
        """        
        if self.__surprise_round and self.__current_init == len(self.__sorted_init) - 1:
            self.__surprise_round = False 
        self.__move(1)
        new_turn_creature = self.__sorted_init[self.__current_init][0]
        new_turn_creature.new_turn()
        if new_turn_creature.should_skip_turn():
            self.move_forward()
    
    def is_surprise_round(self) -> bool:
        """A getter for __surprise_round.

        Returns:
            bool: Returns True if it is a surprise round, False otherwise. 
        """        
        return self.__surprise_round
        
    def move_backward(self) -> None :
        """Moves __current_init backwards.
        """
        self.__move(-1)
        

def sort_key_on_roll(tup: tuple[Initiative_Items, int]) -> int:
    """ A key function so (Creature, int) tuples return int to ensure Python sort functions according to class needs.

    Args:
        tup (tuple[Creature, int]): A Creature and it's initiative roll.

    Returns:
        int: the roll associated with a Creature
    """    
    return tup[1]