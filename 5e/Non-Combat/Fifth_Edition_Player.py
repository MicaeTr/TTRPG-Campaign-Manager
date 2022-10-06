
def get_fresh_slate():
    def get_no_condition():
        return {"Condition?": False, 
                "Sources": "" , 
                "Duration?":0}
    fresh_slate = {
        "Blinded":get_no_condition(), 
        "Charmed":get_no_condition(),
        "Deafened":get_no_condition(),
        "Frightened":get_no_condition(), 
        "Grappled":get_no_condition(),
        "Incapacitated":get_no_condition(),
        "Invisible":get_no_condition(),
        "Paralyzed":get_no_condition(), 
        "Petrified":get_no_condition(), 
        "Poisoned":get_no_condition(), 
        "Prone":get_no_condition(), 
        "Restrained":get_no_condition(), 
        "Stunned":get_no_condition(), 
        "Unconscious":{"Condition?": False, "DST Success": 0, "DST Fail" :0}, 
        "Exhaustion":{"Condition?": False, "Level?":0}, 
        "Concentration": get_no_condition(),
    }
    return fresh_slate
    
""" Fresh slate is the status of a character when they have no conditions. 
    The format of the conditions are "Condition?" which is a boolean, Sources? which is a 
    string that has the source,and Duration which is the integer number of rounds that the 
    condition will last unless it is removed. There are special conditons such as 
    Unconcious which saves the number of Death Saving Throw Successes and 
    Failures, exhaustion which keeps track of the levels of exhaustion, 
    and concentration which keeps track of the spells that they are concentrationg on 
    via the source."""

def condition_meanings(condition):
    pass
"""Condition Meanings gives you the text on the specific condition 
"""

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
        fresh_slate_local = get_fresh_slate()
        self.conditions = fresh_slate_local
        
    def gain_condition(self,condition_name, source, duration):
        con_dict = self.conditions[condition_name]
        con_dict["Condition?"] = True
        if condition_name == "Exhausted":
            con_dict["Level?"] = 1
        if condition_name == "Unconcious":
            pass
        else:
            con_dict["Sources?"] = source
            con_dict["Duration?"] = duration
    
    def loose_condition(self, condition_name):
        con_dict = self.conditions[condition_name]
        con_dict["Condition?"] = False
        if condition_name == "Exhausted":
            con_dict["Level?"] = 0
        if condition_name == "Unconcious":
            con_dict["DST Success"] = 0
            con_dict["DST Fail"] = 0 
        else:
            con_dict["Sources?"] = ""
            con_dict["Duration?"] = 0
            
    def death_saving_through(self, did_it_succeed):
        con_dict = self.conditions["Unconcious"]
        if did_it_succeed:
            con_dict["DST Success"] += 1
        else:
            con_dict["DST Fail"] += 1
    
    def increase_exhaustion(self):
        con_dict = self.conditions["Exhaustion"]
        con_dict["Level?"] += 1
