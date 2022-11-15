from Fifth_Edition_Player import Fifth_Edition_Player

"""
This class keeps track of initiative according to D&D 5e rules. This also can insert Legendary Actions
into the initiative order so that GMs do not forget that legendary actions are available to them
"""

class Fifth_Edition_Initiative:

    def __init__(self, tuple):
        self.initial_initiative = []
        self.initiative_counter = 0
        self.initial_initiative.append(tuple)
        # Tuple is Number, String
        self.sorted_init = self.initial_initiative
        self.original = self.initial_initiative 
    
    def clear_initial_initiative(self):
        self.initial_initiative = []
    
    def update(self):
        self.initial_initiative.sort(reverse=True)
        true_init = []
        for x,y in self.initial_initiative:
            true_init.append(y) #for when the tuples are changed into players
        self.sorted_init = true_init
        self.original = self.initial_initiative 
        self.clear_initial_initiative()
    
    def redefine_self(self):
        self.initial_initiative = self.original
        self.update()
    
    def add_to_init(self, tuple):
        self.original.append(tuple)
        self.redefine_self()
    
    def go_forward(self):
        self.initiative_counter += 1
        self.initiative_counter = self.initiative_counter % len(self.sorted_init)
    
    def go_backward(self):
        self.initiative_counter -= 1
        if self.initiative_counter == -1 :
            self.initiative_counter = len (self.sorted_init)
            self.initiative_counter -= 1
    
    def get_current_person(self):
        current = self.sorted_init[self.initiative_counter]
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
                if self.initiative_counter > 0 :
                    self.initiative_counter -= 1
        except ValueError:
            pass