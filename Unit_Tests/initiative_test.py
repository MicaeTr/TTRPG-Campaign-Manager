import sys
import os
import unittest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
from Fifth_Edition_Dungeons_And_Dragons.Combat.Fifth_Edition_Creature import Fifth_Edition_Creature as Creature 
from Fifth_Edition_Dungeons_And_Dragons.Combat.Fifth_Edition_Initiative import Fifth_Edition_Initiative as Initiative
from Fifth_Edition_Dungeons_And_Dragons.Non_Combat.Fifth_Edition_Player import Fifth_Edition_Player as Player


class TestInitiative(unittest.TestCase):
    """ A class to perform unit tests and verify the expected behavior of the Fifth_Edition_Initiative class.
    """
    
    def setUp(self):
        athena = Player("Artificer", "Athena", 5, -1)
        zeus = Player("Fighter", "Zeus", 5, -1)
        apollo  = Player("Bard", "Apollo", 5, 4) 
        artemis = Player("Ranger", "Artemis", 5, 5)
        aries = Player("Barbarian", "Aries", 10, 0)
        hecate = Player("Wizard", "Hecate", 7, 10)
        iris = Player("Rogue", "Iris", 8, 5)
        demeter = Player("Artificer", "Demeter", 8, 2)
        hermes = Player("Rogue", "Hermes", 7, 2)
        poseidon = Player("Fighter", "Poseidon", 8, 6) 
        venus = Player("Bard", "Venus", 5, -1)
        hestia = Player("Bard", "Hestia", 5, -2)
        
        self.default_initiative = Initiative()
        self.sorted_by_dex = Initiative(sort_on_dex=True)
        self.surprised_initiative = Initiative(surprise_round=True)
        self.surprised_and_sorted_by_dex_initiative = Initiative(sort_on_dex=True, surprise_round=True)
        
        self.two_same_roll_initial_top = [(zeus, 15),(apollo, 20), (athena,2), (artemis, 20)]
        self.two_same_roll_initial_middle = [(zeus, 20), (apollo, 15), (athena, 2), (artemis, 15)] 
        self.two_same_roll_initial_bottom = [(zeus, 20), (apollo, 10), (athena, 15), (artemis, 10)] 
        self.three_same_roll_different_dex_initial = [(apollo, 10), (athena, 5), (demeter, 15), 
                                                      (artemis, 5), (poseidon, 17), (hermes, 5)] 
        self.three_same_roll_same_dex_initial = [(apollo, 17), (zeus, 15), (artemis, 18),
                                                 (athena, 15), (hermes, 14), (iris, 15)] 

        self.small_rolled_initiative_in_order = [(zeus, 15), (athena, 2)] 
        self.small_rolled_initiative_out_of_order = [(athena, 2), (zeus, 15)] 

        self.large_rolled_initiative_in_order = [(athena, 30), (zeus, 27), (apollo, 23), 
                                                 (artemis, 20), (aries, 17), (hecate, 15), 
                                                 (iris, 10), (demeter, 5), (poseidon, 3) ,(hermes, 1)] 
        
        self.removal_initiative_list = [(zeus, 20), (apollo, 17), (artemis, 15), (athena, 10)]
        self.removal_initiative_list_copy = [(zeus, 20), (apollo, 17), (artemis, 15), (athena, 10)] 
        
        self.remove_three_initiative_list = [(zeus, 25), (apollo, 23),
                                             (artemis, 20), (athena, 15), 
                                             (iris, 10), (hermes,5)] 
        self.remove_three_initiative_list_copy = [(zeus, 25), (apollo, 23),
                                                  (artemis, 20), (athena, 15), 
                                                  (iris, 10), (hermes,5)] 
        
        self.add_during_combat_list_base = [(zeus, 20), (hermes, 15), (iris, 10)] 
        self.add_during_combat_list_base_copy = [(zeus, 20), (hermes, 15), (iris, 10)] 
        self.add_during_combat_list_goal = [(zeus, 20), (hermes, 15), (iris, 10)] 
        self.add_during_combat_no_conflict_list = [(apollo, 25), (hecate, 17), (aries, 8)] 
        self.add_during_combat_conflict_different_dex = [(apollo, 20), (hecate, 15), (aries, 10)] 
        self.add_during_combat_conflict_same_dex_as_list = [(athena, 20), (demeter, 15), (artemis,10)] 
        self.add_during_combat_conflict_same_dex_as_current = [(athena, 20),(venus, 20)]
        
        self.hestia = hestia
        self.artemis = artemis
        self.apollo = apollo
        self.zeus = zeus
        self.athena = athena
        self.poseidon = poseidon
        self.demeter = demeter
        self.hermes = hermes
        self.hecate = hecate
        self.aries = aries
        self.iris = iris
        self.venus = venus

    def tearDown(self):
        self.default_initiative = None
        self.sorted_by_dex = None
        self.surprised_initiative = None
        self.surprised_and_sorted_by_dex_initiative = None
        self.two_same_roll_initial_top = None
        self.two_same_roll_initial_middle = None
        self.two_same_roll_initial_bottom = None
        self.three_same_roll_different_dex_initial = None
        self.three_same_roll_same_dex_initial = None 
        self.small_rolled_initiative_in_order = None
        self.small_rolled_initiative_out_of_order = None
        self.large_rolled_initiative_in_order = None
        self.removal_initiative_list = None
        self.removal_initiative_list_copy = None
        self.remove_three_initiative_list = None
        self.remove_three_initiative_list_copy = None
        self.add_during_combat_list_base = None
        self.add_during_combat_list_base_copy = None
        self.add_during_combat_list_goal = None
        self.add_during_combat_no_conflict_list = None
        self.add_during_combat_conflict_different_dex = None
        self.add_during_combat_conflict_same_dex_as_list = None
        self.add_during_combat_conflict_same_dex_as_current = None
        
        self.hestia = None
        self.artemis = None
        self.apollo = None
        self.zeus = None
        self.athena = None
        self.poseidon = None
        self.demeter = None
        self.hermes = None
        self.hecate = None
        self.aries = None
        self.iris = None
        self.venus = None

    def test_is_surprise_round(self):
        self.assertTrue(self.surprised_initiative.is_surprise_round())
        self.assertFalse(self.default_initiative.is_surprise_round())
        self.assertTrue(self.surprised_and_sorted_by_dex_initiative.is_surprise_round())
        
    def test_is_surprised_round_move_forward_still_surprised(self):
        self.surprised_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_and_sorted_by_dex_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.assertTrue(self.surprised_initiative.is_surprise_round())
        
    def test_is_surprised_round_move_forward_until_not_surprised(self):
        self.surprised_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_and_sorted_by_dex_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_initiative.move_forward()
        self.surprised_initiative.move_forward()
        self.surprised_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.assertFalse(self.surprised_initiative.is_surprise_round())
        self.assertFalse(self.surprised_and_sorted_by_dex_initiative.is_surprise_round())
        
    def test_is_surprised_round_move_forward_and_backward_still_surprised(self):
        self.surprised_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_and_sorted_by_dex_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_initiative.move_forward()
        self.surprised_initiative.move_backward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_backward()
        self.surprised_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.assertTrue(self.surprised_initiative.is_surprise_round())
        self.assertTrue(self.surprised_and_sorted_by_dex_initiative.is_surprise_round())
        
    def test_is_surprised_round_move_forward_and_backward_until_not_surprised(self):
        self.surprised_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_and_sorted_by_dex_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.surprised_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_backward()
        self.surprised_initiative.move_backward()
        self.surprised_initiative.move_forward()
        self.surprised_initiative.move_forward()
        self.surprised_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.surprised_and_sorted_by_dex_initiative.move_forward()
        self.assertFalse(self.surprised_initiative.is_surprise_round())
        self.assertFalse(self.surprised_and_sorted_by_dex_initiative.is_surprise_round())

    def test_initial_add_small(self): 
        self.default_initiative.initial_add(self.small_rolled_initiative_out_of_order)
        sorted_list = self.default_initiative.full_initiative_order()
        self.assertEqual(sorted_list, self.small_rolled_initiative_in_order)
    
    def test_initial_add_large(self):
        large_rolled_initiative_out_of_order = [(self.hermes, 1) , (self.zeus, 27), (self.hecate, 15) , 
                                                 (self.aries, 17), (self.apollo, 23), (self.artemis, 20), 
                                                 (self.demeter, 5), (self.iris, 10), (self.poseidon, 3) ,(self.athena, 30)]
        self.default_initiative.initial_add(large_rolled_initiative_out_of_order)
        sorted_list = self.default_initiative.full_initiative_order()
        self.assertEqual(sorted_list, self.large_rolled_initiative_in_order)
    
    def test_initial_add_same_rolls_different_dex_sorted_by_dex_top(self):
        self.sorted_by_dex.initial_add(self.two_same_roll_initial_top)
        sorted_list = self.sorted_by_dex.full_initiative_order()
        two_same_roll_sorted_by_dex_top = [(self.artemis, 20), (self.apollo, 20), (self.zeus, 15), (self.athena, 2)] 
        self.assertEqual(sorted_list, two_same_roll_sorted_by_dex_top)
        
    def test_initial_add_same_rolls_different_dex_sorted_by_dex_middle(self):
        self.sorted_by_dex.initial_add(self.two_same_roll_initial_middle)
        sorted_list = self.sorted_by_dex.full_initiative_order()
        two_same_roll_sorted_by_dex_middle = [(self.zeus, 20), (self.artemis, 15), (self.apollo, 15), (self.athena, 2)]
        self.assertEqual(sorted_list, two_same_roll_sorted_by_dex_middle)

    def test_initial_add_same_rolls_different_dex_sorted_by_dex_bottom(self):
        self.sorted_by_dex.initial_add(self.two_same_roll_initial_bottom)
        sorted_list = self.sorted_by_dex.full_initiative_order()
        two_same_roll_sorted_by_dex_bottom = [(self.zeus, 20), (self.athena, 15), (self.artemis, 10), (self.apollo, 10)] 
        self.assertEqual(sorted_list, two_same_roll_sorted_by_dex_bottom)
    
    def test_initial_add_same_rolls_different_dex_not_sorted_by_dex_top(self):
        self.default_initiative.initial_add(self.two_same_roll_initial_top)
        sorted_list = self.default_initiative.full_initiative_order()
        two_same_roll_not_sorted_by_dex_top = [(self.apollo, 20), (self.artemis, 20), (self.zeus, 15), (self.athena, 2)]
        self.assertEqual(sorted_list, two_same_roll_not_sorted_by_dex_top)
    
    def test_initial_add_same_rolls_different_dex_not_sorted_by_dex_middle(self):
        self.default_initiative.initial_add(self.two_same_roll_initial_middle)
        sorted_list = self.default_initiative.full_initiative_order()
        two_same_roll_not_sorted_by_dex_middle = [(self.zeus, 20), (self.apollo, 15), (self.artemis, 15), (self.athena, 2)] 
        self.assertEqual(sorted_list, two_same_roll_not_sorted_by_dex_middle)
    
    def test_initial_add_same_rolls_different_dex_not_sorted_by_dex_bottom(self):
        self.default_initiative.initial_add(self.two_same_roll_initial_bottom)
        sorted_list = self.default_initiative.full_initiative_order()
        two_same_roll_not_sorted_by_dex_bottom = [(self.zeus, 20), (self.athena, 15), (self.apollo, 10), (self.artemis, 10)] 
        self.assertEqual(sorted_list, two_same_roll_not_sorted_by_dex_bottom)
    
    def test_initial_add_three_creatures_same_roll_different_dex_sorted_by_dex(self):
        self.sorted_by_dex.initial_add(self.three_same_roll_different_dex_initial)
        sorted_list = self.sorted_by_dex.full_initiative_order()
        three_same_roll_different_dex_sorted_by_dex = [(self.poseidon, 17),(self.demeter, 15),(self.apollo, 10), 
                                                            (self.artemis, 5), (self.hermes, 5), (self.athena, 5)] 
        self.assertEqual(sorted_list, three_same_roll_different_dex_sorted_by_dex)
    
    def test_initial_add_three_creatures_same_roll_different_dex_not_sorted_by_dex(self):
        self.default_initiative.initial_add(self.three_same_roll_different_dex_initial)
        sorted_list = self.default_initiative.full_initiative_order()
        three_same_roll_different_dex_not_sorted_by_dex = [(self.poseidon, 17),(self.demeter, 15),(self.apollo, 10), 
                                                            (self.athena, 5), (self.artemis, 5), (self.hermes, 5)]
        self.assertEqual(sorted_list, three_same_roll_different_dex_not_sorted_by_dex)
    
    def test_initial_add_three_creatures_same_roll_same_dex_sorted_by_dex(self):
        self.sorted_by_dex.initial_add(self.three_same_roll_same_dex_initial)
        sorted_list = self.sorted_by_dex.full_initiative_order()
        three_same_roll_same_dex_sorted_by_dex = [(self.artemis, 18),(self.apollo, 17), (self.iris, 15), 
                                                       (self.zeus, 15), (self.athena, 15), (self.hermes, 14)]
        self.assertEqual(sorted_list, three_same_roll_same_dex_sorted_by_dex)
    
    def test_initial_add_three_creatures_same_roll_same_dex_not_sorted_by_dex(self):
        self.default_initiative.initial_add(self.three_same_roll_same_dex_initial)
        sorted_list = self.default_initiative.full_initiative_order()
        three_same_roll_same_dex_not_sorted_by_dex = [(self.artemis, 18),(self.apollo, 17), (self.zeus, 15), 
                                                           (self.athena, 15), (self.iris, 15), (self.hermes, 14)] 
        self.assertEqual(sorted_list, three_same_roll_same_dex_not_sorted_by_dex)
    
    def test_string_representation(self): 
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        string_init = " \n"
        for item in self.small_rolled_initiative_in_order:
            string_init += f"{item}\n"
        string_representation = f"Full Initiative Order:{string_init}\nCurrent Initiative Index: 0, \
            Surprise Round: False, Sort On Dex: False"
        string_from_default_initiative = f"{self.default_initiative}"
        self.assertEqual(string_representation, string_from_default_initiative)
    
    def test_current_initiative_order_as_list_of_players(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        order = self.default_initiative.current_initiative_order()
        self.assertEqual(order, self.small_rolled_initiative_in_order)
    
    def test_current_initiative_order_as_list_of_players_after_a_move(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.default_initiative.move_forward()
        order = self.default_initiative.current_initiative_order()
        self.assertEqual(order, self.small_rolled_initiative_out_of_order)
    
    def test_current_initiative_order_as_list_of_players_after_a_move_backwards(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_out_of_order)
        self.default_initiative.move_backward()
        self.default_initiative.move_backward()
        order = self.default_initiative.current_initiative_order()
        self.assertEqual(order, self.small_rolled_initiative_in_order)
    
    def test_current_initiative_order_as_list_of_players_after_moving_forward_then_backwards(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.default_initiative.move_forward()
        self.default_initiative.move_backward()
        order = self.default_initiative.current_initiative_order()
        self.assertEqual(order, self.small_rolled_initiative_in_order)
    
    def test_current_initiative_order_as_list_of_players_back_at_top_of_initiative(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        order = self.default_initiative.current_initiative_order()
        self.assertEqual(order, self.small_rolled_initiative_in_order)
        
    def test_current_item(self):
        self.default_initiative.initial_add(self.large_rolled_initiative_in_order)
        from_default = self.default_initiative.current_item()
        self.assertEqual(from_default, self.large_rolled_initiative_in_order[0])
    
    def test_move_forward_and_current_item(self):
        self.default_initiative.initial_add(self.large_rolled_initiative_in_order)
        self.default_initiative.move_forward()
        from_default = self.default_initiative.current_item()
        self.assertEqual(from_default, self.large_rolled_initiative_in_order[1])
    
    def test_move_backwards_and_current_item(self):
        self.default_initiative.initial_add(self.large_rolled_initiative_in_order)
        self.default_initiative.move_backward()
        from_default = self.default_initiative.current_item()
        self.assertEqual(from_default, self.large_rolled_initiative_in_order[-1])
    
    def test_remove_during_combat_one_top_of_initiative_removal_equal_to_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        remove = [self.removal_initiative_list_copy[0]]
        current_item_after_removal = self.removal_initiative_list_copy[1]
        self.default_initiative.remove_during_combat(remove)
        new_initiative = self.default_initiative.full_initiative_order()
        new_creature = self.default_initiative.current_item()
        self.assertEqual(current_item_after_removal, new_creature)
        self.assertEqual(new_initiative, self.removal_initiative_list_copy[1::])
    
    def test_remove_during_combat_one_top_of_initiative_removal_more_than_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        remove = [self.removal_initiative_list_copy[2]]
        current_item_after_removal = self.removal_initiative_list_copy[0]
        self.default_initiative.remove_during_combat(remove)
        new_initiative = self.default_initiative.full_initiative_order()
        new_creature = self.default_initiative.current_item()
        initiative_after_removal = [self.removal_initiative_list_copy[0], 
                                    self.removal_initiative_list_copy[1],
                                    self.removal_initiative_list_copy[3]]
        self.assertEqual(current_item_after_removal, new_creature)
        self.assertEqual(new_initiative,initiative_after_removal)
    
    def test_remove_during_combat_one_middle_of_initiative_less_than_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        remove = [self.removal_initiative_list_copy[0]]
        self.default_initiative.remove_during_combat(remove)
        initiative_after_removal = self.default_initiative.full_initiative_order()
        creature_after_removal = self.default_initiative.current_item()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = self.removal_initiative_list_copy[1::]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(initiative_after_removal, goal_initiative)
    
    def test_remove_during_combat_one_middle_of_initiative_equal_to_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        remove = [self.removal_initiative_list_copy[1]]
        self.default_initiative.remove_during_combat(remove)
        initiative_after_removal = self.default_initiative.full_initiative_order()
        creature_after_removal = self.default_initiative.current_item()
        goal_creature = self.removal_initiative_list_copy[2]
        goal_initiative = [self.removal_initiative_list_copy[0], 
                           self.removal_initiative_list_copy[2], 
                           self.removal_initiative_list_copy[3]]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(initiative_after_removal, goal_initiative)
        
    def test_remove_during_combat_one_middle_of_initiative_more_than_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        remove = [self.removal_initiative_list_copy[2]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = [self.removal_initiative_list_copy[0], 
                           self.removal_initiative_list_copy[1],
                           self.removal_initiative_list_copy[3]]
        self.assertEqual(creature_after_removal, goal_creature)
        self.assertEqual(initiative_after_removal, goal_initiative)
    
    def test_remove_during_combat_one_bottom_of_initiative_less_than_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.removal_initiative_list_copy[2]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[3]
        goal_initiative = [self.removal_initiative_list_copy[0], 
                           self.removal_initiative_list_copy[1], 
                           self.removal_initiative_list_copy[3]]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(goal_initiative, initiative_after_removal)
        
    def test_remove_during_combat_one_bottom_of_initiative_equal_to_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.removal_initiative_list_copy[3]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[0]
        goal_initiative = self.removal_initiative_list_copy[:3]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(goal_initiative, initiative_after_removal)
    
    def test_remove_during_combat_multiple_top_of_initiative_removal_contains_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        remove = [self.remove_three_initiative_list_copy[0],
                  self.remove_three_initiative_list_copy[1], 
                  self.remove_three_initiative_list_copy[2]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[3]
        goal_initiative = self.remove_three_initiative_list_copy[3:]
        self.assertEqual(creature_after_removal, goal_creature)
        self.assertEqual(goal_initiative, initiative_after_removal)
    
    def test_remove_during_combat_multiple_top_of_initiative_removal_more_than_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        remove = [self.remove_three_initiative_list_copy[3],
                  self.remove_three_initiative_list_copy[4], 
                  self.remove_three_initiative_list_copy[5]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[0]
        goal_initiative = self.remove_three_initiative_list_copy[:3]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(goal_initiative, initiative_after_removal)
        
    def test_remove_during_combat_multiple_middle_of_initiative_less_than_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[3], 
                  self.remove_three_initiative_list_copy[1], 
                  self.remove_three_initiative_list_copy[2]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_creature = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[4]
        goal_initiative = [self.remove_three_initiative_list_copy[0], 
                           self.remove_three_initiative_list_copy[4], 
                           self.remove_three_initiative_list_copy[5]]
        self.assertEqual(initiative_after_creature, goal_initiative)
        self.assertEqual(creature_after_removal, goal_creature)
    
    def test_remove_during_combat_multiple_middle_of_initiative_contains_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[1], 
                  self.remove_three_initiative_list_copy[2], 
                  self.remove_three_initiative_list_copy[3]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[4]
        goal_initiative = [self.remove_three_initiative_list_copy[0], 
                           self.remove_three_initiative_list_copy[4], 
                           self.remove_three_initiative_list_copy[5]]
        self.assertEqual(creature_after_removal, goal_creature)
        self.assertEqual(initiative_after_removal, goal_initiative)
    
    def test_remove_during_combat_multiple_middle_of_initiative_more_than_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[2], 
                  self.remove_three_initiative_list_copy[3], 
                  self.remove_three_initiative_list_copy[4]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[1]
        goal_initiative = [self.remove_three_initiative_list_copy[0], 
                           self.remove_three_initiative_list_copy[1], 
                           self.remove_three_initiative_list_copy[5]]
        self.assertEqual(creature_after_removal, goal_creature)
        self.assertEqual(initiative_after_removal, goal_initiative)
        
    def test_remove_during_combat_multiple_bottom_of_initiative_less_than_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[1], 
                  self.remove_three_initiative_list_copy[2], 
                  self.remove_three_initiative_list_copy[3]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[5]
        goal_initiative = [self.remove_three_initiative_list_copy[0], 
                           self.remove_three_initiative_list_copy[4], 
                           self.remove_three_initiative_list_copy[5]]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(goal_initiative, initiative_after_removal)
    
    def test_remove_during_combat_multiple_bottom_of_initiative_contains_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[3], 
                  self.remove_three_initiative_list_copy[4], 
                  self.remove_three_initiative_list_copy[5]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_After_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[0]
        goal_initiative = [self.remove_three_initiative_list_copy[0], 
                           self.remove_three_initiative_list_copy[1], 
                           self.remove_three_initiative_list_copy[2]]
        self.assertEqual(creature_after_removal, goal_creature)
        self.assertEqual(goal_initiative, initiative_After_removal)
    
    def test_remove_during_combat_multiple_surrounding_current(self):
        self.default_initiative.initial_add(self.remove_three_initiative_list)
        self.default_initiative.move_forward()
        remove = [self.remove_three_initiative_list_copy[0], 
                  self.remove_three_initiative_list_copy[2], 
                  self.remove_three_initiative_list_copy[4]]
        self.default_initiative.remove_during_combat(remove)
        creature_after_removal = self.default_initiative.current_item()
        initiative_after_removal = self.default_initiative.full_initiative_order()
        goal_creature = self.remove_three_initiative_list_copy[1]
        goal_initiative = [self.remove_three_initiative_list_copy[1], 
                           self.remove_three_initiative_list_copy[3], 
                           self.remove_three_initiative_list_copy[5]]
        self.assertEqual(goal_creature, creature_after_removal)
        self.assertEqual(goal_initiative, initiative_after_removal)
    
    def test_add_during_combat_one_before_current(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.add_during_combat([self.add_during_combat_no_conflict_list[0]])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        self.add_during_combat_list_goal.insert(0, self.add_during_combat_no_conflict_list[0])
        current_initiative = self.default_initiative.full_initiative_order()
        self.assertEqual(current_item, goal_creature)
        self.assertEqual(self.add_during_combat_list_goal, current_initiative)
    
    def test_add_during_combat_one_at_current_smaller_dex_sorted_by_dex(self):
        self.sorted_by_dex.initial_add(self.add_during_combat_list_base)
        self.sorted_by_dex.add_during_combat([(self.hestia, 20)])
        current_item = self.sorted_by_dex.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.sorted_by_dex.full_initiative_order()
        self.add_during_combat_list_goal.insert(1, (self.hestia, 20))
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
        self.assertEqual(current_item, goal_creature)
        
    def test_add_during_combat_one_at_current_same_dex_sorted_by_dex(self):
        self.sorted_by_dex.initial_add(self.add_during_combat_list_base)
        self.sorted_by_dex.add_during_combat([self.add_during_combat_conflict_same_dex_as_list[0]])
        current_item = self.sorted_by_dex.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.sorted_by_dex.full_initiative_order()
        self.add_during_combat_list_goal.insert(0,self.add_during_combat_conflict_same_dex_as_list[0] )
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
        self.assertEqual(goal_creature, current_item)
    
    def test_add_during_combat_one_at_current_larger_dex_sorted_by_dex(self):
        self.sorted_by_dex.initial_add(self.add_during_combat_list_base)
        self.sorted_by_dex.add_during_combat([self.add_during_combat_conflict_different_dex[0]])
        current_item = self.sorted_by_dex.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.sorted_by_dex.full_initiative_order()
        self.add_during_combat_list_goal.insert(0,self.add_during_combat_conflict_different_dex[0]) 
        self.assertEqual(current_item, goal_creature)
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
    
    def test_add_during_combat_one_at_current_different_dex_not_sorted_by_dex(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.add_during_combat([self.add_during_combat_conflict_different_dex[0]])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.default_initiative.full_initiative_order()
        self.add_during_combat_list_goal.insert(1, self.add_during_combat_conflict_different_dex[0])
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
        self.assertEqual(current_item, goal_creature)
    
    def test_add_during_combat_one_at_current_same_dex_not_sorted_by_dex(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.add_during_combat([self.add_during_combat_conflict_same_dex_as_list[0]])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.default_initiative.full_initiative_order()
        self.add_during_combat_list_goal.insert(1, self.add_during_combat_conflict_same_dex_as_list[0])
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
        self.assertEqual(goal_creature, current_item)
    
    def test_add_during_combat_after_current(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.add_during_combat([self.add_during_combat_no_conflict_list[1]])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.default_initiative.full_initiative_order()
        self.add_during_combat_list_goal.insert(1, self.add_during_combat_no_conflict_list[1])
        self.assertEqual(goal_creature, current_item)
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
    
    def test_add_during_combat_multiple_before_current(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.add_during_combat([self.add_during_combat_no_conflict_list[0], 
                                                   self.add_during_combat_no_conflict_list[1], 
                                                   self.add_during_combat_conflict_different_dex[0]])
        self.add_during_combat_list_goal.insert(0,self.add_during_combat_no_conflict_list[0])
        self.add_during_combat_list_goal.insert(2, self.add_during_combat_conflict_different_dex[0])
        self.add_during_combat_list_goal.insert(3, self.add_during_combat_no_conflict_list[1])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[2]
        current_initiative = self.default_initiative.full_initiative_order()
        self.assertEqual(current_item, goal_creature)
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
    
    def test_add_during_combat_multiple_after_current(self):
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.add_during_combat([self.add_during_combat_no_conflict_list[1], 
                                                   self.add_during_combat_no_conflict_list[2], 
                                                   self.add_during_combat_conflict_different_dex[2]])
        current_item = self.default_initiative.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.default_initiative.full_initiative_order()
        self.add_during_combat_list_goal.insert(1, self.add_during_combat_no_conflict_list[1])
        self.add_during_combat_list_goal.insert(4, self.add_during_combat_conflict_different_dex[2])
        self.add_during_combat_list_goal.insert(5, self.add_during_combat_no_conflict_list[2])
        self.assertEqual(goal_creature, current_item)
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
    
    def test_add_during_combat_multiple_contains_current_all_with_same_roll_different_dex_sort_by_dex(self):
        self.sorted_by_dex.initial_add(self.add_during_combat_list_base)
        hestia_initiative = (self.hestia, 20)
        self.sorted_by_dex.add_during_combat([self.add_during_combat_conflict_different_dex[0], hestia_initiative])
        current_item = self.sorted_by_dex.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        self.add_during_combat_list_goal.insert(0, self.add_during_combat_conflict_different_dex[0])
        self.add_during_combat_list_goal.insert(2, hestia_initiative)
        current_initiative = self.sorted_by_dex.full_initiative_order()
        self.assertEqual(goal_creature, current_item)
        self.assertEqual(self.add_during_combat_list_goal, current_initiative)
    
    def test_add_during_combat_multiple_contains_current_all_with_same_roll_same_dex_sort_by_dex(self):
        self.sorted_by_dex.initial_add(self.add_during_combat_list_base)
        self.sorted_by_dex.add_during_combat(self.add_during_combat_conflict_same_dex_as_current)
        self.add_during_combat_list_goal.insert(0, self.add_during_combat_conflict_same_dex_as_current[1])
        self.add_during_combat_list_goal.insert(1, self.add_during_combat_conflict_same_dex_as_current[0])
        current_item = self.sorted_by_dex.current_item()
        goal_creature = self.add_during_combat_list_base_copy[0]
        current_initiative = self.sorted_by_dex.full_initiative_order()
        self.assertEqual(current_initiative, self.add_during_combat_list_goal)
        self.assertEqual(current_item, goal_creature)
    
    def test_manual_change_old_is_before_current_new_is_after_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward() 
        self.default_initiative.manual_change(0, 3)
        creature_after_move = self.default_initiative.current_item()
        initiative_after_move = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = [self.removal_initiative_list_copy[1], 
                           self.removal_initiative_list_copy[2], 
                           self.removal_initiative_list_copy[3],
                           self.removal_initiative_list_copy[0]]
        self.assertEqual(goal_creature, creature_after_move)
        self.assertEqual(goal_initiative, initiative_after_move)
    
    def test_manual_change_old_is_after_current_new_is_before_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.manual_change(3,0)
        creature_after_change = self.default_initiative.current_item()
        initiative_after_change = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = [self.removal_initiative_list_copy[3], 
                           self.removal_initiative_list_copy[0],
                           self.removal_initiative_list_copy[1],
                           self.removal_initiative_list_copy[2]]
        self.assertEqual(creature_after_change, goal_creature)
        self.assertEqual(goal_initiative, initiative_after_change)
    
    def test_manual_change_all_before_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.manual_change(0,1)
        creature_after_move = self.default_initiative.current_item()
        initiative_after_move = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[2]
        goal_initiative = [self.removal_initiative_list_copy[1],
                           self.removal_initiative_list_copy[0],
                           self.removal_initiative_list_copy[2],
                           self.removal_initiative_list_copy[3]]
        self.assertEqual(goal_initiative, initiative_after_move)
        self.assertEqual(goal_creature, creature_after_move)
    
    def test_manual_change_all_after_current(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.manual_change(2, 3)
        creature_after_move = self.default_initiative.current_item()
        initiative_after_move = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[0]
        goal_initiative = [self.removal_initiative_list_copy[0],
                           self.removal_initiative_list_copy[1],
                           self.removal_initiative_list_copy[3],
                           self.removal_initiative_list_copy[2]]
        self.assertEqual(goal_creature, creature_after_move)
        self.assertEqual(goal_initiative, initiative_after_move)
    
    def test_manual_change_move_current_down(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.manual_change(0, 2)
        creature_after_move = self.default_initiative.current_item()
        initiative_after_move = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = [self.removal_initiative_list_copy[1],
                           self.removal_initiative_list_copy[2],
                           self.removal_initiative_list_copy[0],
                           self.removal_initiative_list_copy[3]]
        self.assertEqual(goal_creature, creature_after_move)
        self.assertEqual(goal_initiative, initiative_after_move)
        
    def test_manual_change_move_current_up(self):
        self.default_initiative.initial_add(self.removal_initiative_list)
        self.default_initiative.move_forward()
        self.default_initiative.move_forward()
        self.default_initiative.manual_change(2, 0)
        creature_after_change = self.default_initiative.current_item()
        initiative_after_move = self.default_initiative.full_initiative_order()
        goal_creature = self.removal_initiative_list_copy[1]
        goal_initiative = [self.removal_initiative_list_copy[2],
                            self.removal_initiative_list_copy[0],
                            self.removal_initiative_list_copy[1],
                            self.removal_initiative_list_copy[3]]
        self.assertEqual(goal_creature, creature_after_change)
        self.assertEqual(goal_initiative, initiative_after_move)
    
    def test_manual_change_error(self):
        self.default_initiative.initial_add(self.small_rolled_initiative_in_order)
        self.assertRaises(IndexError, self.default_initiative.manual_change, 0, 3)
        
    def test_manual_change_and_add_during_combat(self):
        goal_list = [self.add_during_combat_list_base_copy[1], 
                     self.add_during_combat_list_base_copy[2],
                     self.add_during_combat_no_conflict_list[2], 
                     self.add_during_combat_list_base_copy[0]]
        self.default_initiative.initial_add(self.add_during_combat_list_base) 
        self.default_initiative.manual_change(0,2)
        self.default_initiative.add_during_combat([self.add_during_combat_no_conflict_list[2]])
        current_initiative = self.default_initiative.full_initiative_order()
        self.assertEqual(goal_list, current_initiative)
    
    def test_manual_change_and_remove_during_combat(self):
        goal_list = [self.add_during_combat_list_base_copy[1], 
                     self.add_during_combat_list_base_copy[0]]
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.manual_change(0,2)
        self.default_initiative.remove_during_combat([self.add_during_combat_list_base_copy[2]])
        initiative_list = self.default_initiative.full_initiative_order()
        self.assertEqual(initiative_list, goal_list)
    
    def test_manual_change_remove_changed_item(self):
        goal_list = [self.add_during_combat_list_base_copy[1], 
                     self.add_during_combat_list_base_copy[2]]
        self.default_initiative.initial_add(self.add_during_combat_list_base)
        self.default_initiative.manual_change(0,2)
        self.default_initiative.remove_during_combat([self.add_during_combat_list_base_copy[0]])
        initiative_list = self.default_initiative.full_initiative_order()
        self.assertEqual(goal_list, initiative_list)
    
    def test_initial_add_with_one_item_and_multiple_added_during_combat(self):
        initial_add_list = [(self.hestia, 5)]
        add_during_combat_list = [(self.poseidon, 10), (self.athena, 2)]
        self.default_initiative.initial_add(initial_add_list)
        self.default_initiative.add_during_combat(add_during_combat_list)
        goal_list = [(self.poseidon, 10), (self.hestia, 5), (self.athena, 2)]
        current_list = self.default_initiative.full_initiative_order()
        self.assertEqual(goal_list, current_list)
        
    def test_remove_during_combat_error(self):
        self.default_initiative.initial_add([(self.hestia, 5)])
        self.default_initiative.remove_during_combat([(self.hestia, 5)])
        self.assertRaises(ValueError, self.default_initiative.remove_during_combat, [(self.athena, 2)])
    
    def test_manual_change_and_add_multiple_during_combat(self):
        goal_list = [(self.athena, 21), (self.hecate, 15),(self.hermes, 10), 
                     (self.zeus, 20),(self.aries, 5), (self.iris, 3), (self.venus, 1)]
        initial_add_list = [(self.zeus, 20), (self.hermes, 10), (self.iris, 3)]
        add_during_combat_list = [(self.athena, 21), (self.hecate, 15), (self.aries, 5), (self.venus, 1)]
        self.default_initiative.initial_add(initial_add_list)
        self.default_initiative.manual_change(0, 1)
        self.default_initiative.add_during_combat(add_during_combat_list)
        current_list = self.default_initiative.full_initiative_order()
        self.assertEqual(goal_list, current_list)
    
    def test_manual_change_changes_are_in_the_middle(self):
        initial_add_list = [(self.zeus, 20), (self.hermes, 10), (self.iris, 3), (self.venus, 1)]
        goal_list = [(self.zeus, 20), (self.iris, 3),(self.hermes, 10),  (self.venus, 1)]
        self.default_initiative.initial_add(initial_add_list)
        self.default_initiative.manual_change(1,2)
        current_list = self.default_initiative.full_initiative_order()
        self.assertEqual(current_list, goal_list)


if __name__ == '__main__':
    unittest.main()
