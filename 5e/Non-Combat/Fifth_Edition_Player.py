from Conditions import Conditions
from Utils import Condition_Names

class Fifth_Edition_Player():
    """ A definition and class containing all of the methods necessary for a 5th Edition D&D
    player. This class is relatively simple and includes statuses such as conditions
    & Death saving throws. This is a place holder for your players and helps you and them 
    keep track of statuses and conditions that are difficult to keep track of while
    in battle"""
    
    def __init__(self, fifth_class, name, level):
        self.fifth_class = fifth_class # string
        self.name = name # string
        self.level = level  # number
        self.conditions = Conditions()
        
    def gain_condition(self,condition_name, source, duration):
        if condition_name == Condition_Names.EXHAUSTED:
            self.conditions.exhaustion.gain_condition()
            self.conditions.exhaustion.gain_a_level()
        else:
            self.conditions.gain_condition(condition_name=condition_name, source=source, duration= duration)
    
    def loose_condition(self, condition_name):
        self.conditions.loose_condition(condition_name=condition_name)
            
    def death_saving_through(self, did_it_succeed):
        if did_it_succeed:
            self.conditions.unconscious.success()
        else:
            self.conditions.unconscious.fail()
    
    def increase_exhaustion(self):
        self.conditions.exhaustion.gain_a_level()
