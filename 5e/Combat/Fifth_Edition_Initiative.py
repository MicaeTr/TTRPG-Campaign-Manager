from os import remove
from Fifth_Edition_Player import Fifth_Edition_Player


initial_initiative = []
initiative_counter = 0

"""
This class keeps track of initiative according to D&D 5e rules. This also can insert Legendary Actions
into the initiative order so that GMs do not forget that legendary actions are available to them
"""

class Fifth_Edition_Initative:

    def __init__(self, tuple):
        global initial_initiative
        initial_initiative.append(tuple)
        # Tuple is Number, String
        self.sorted_init = initial_initiative
        self.original = initial_initiative 
    
    def clear_initial_initiative(self):
        global initial_initiatve
        initial_initiative = []
    
    def update(self):
        global initial_initiative
        initial_initiative.sort(reverse=True)
        true_init = []
        for x,y in initial_initiative:
            true_init.append(y) #for when the tuples are changed into players
        self.sorted_init = true_init
        self.original = initial_initiative 
        self.clear_initial_initiative()
    
    def redefine_self(self):
        global initial_initiative
        initial_initiative = self.original
        self.update()
    
    def add_to_init(self, tuple):
        self.original.append(tuple)
        self.redefine_self()
    
    def go_forward(self):
        global initiative_counter
        initiative_counter += 1
        if len(self.sorted_init) == initiative_counter:
            initiative_counter = 0
    
    def go_backward(self):
        global initiative_counter
        initiative_counter -= 1
        if initiative_counter == -1 :
            initiative_counter = len (self.sorted_init)
            initiative_counter -= 1
    
    def get_current_person(self):
        global initiative_counter
        current = self.sorted_init[initiative_counter]
        return current
    
    def insert_legendary_actions(self, monster_name):
        insert_here = 1
        original_length = len(self.sorted_init)
        double_len = 2 * original_length
        max_index = double_len - 1
        while insert_here <= max_index:
            self.sorted_init.insert(insert_here, monster_name)
            insert_here += 2
    
    def remove_all_legendary_actions(self, monster_name):
        try:
            while True:
                self.sorted_init.remove(monster_name)
                global initiative_counter
                if initiative_counter > 0 :
                    initiative_counter -= 1
        except ValueError:
            pass