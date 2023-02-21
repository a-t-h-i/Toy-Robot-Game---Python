import unittest
from world.obstacles import get_obstacles
from world import obstacles

class test_obstacles(unittest.TestCase):
    obstacles.my_obstacles = get_obstacles()    
    def test_get_obstacles(self):
        self.assertEqual(bool(obstacles.my_obstacles), False)

    def test_position_blocked(self):
        obstacles.my_obstacles = [[(13, 162), (17, 162), (17, 166), (13, 166)]]
        self.assertFalse(obstacles.is_position_blocked(50, 10))
        self.assertFalse(obstacles.is_position_blocked(100,200))
        self.assertTrue(obstacles.is_position_blocked(14,163))
        self.assertTrue(obstacles.is_position_blocked(15,165))

    
    def test_path_blocked(self):
        obstacles.my_obstacles = [[(13, 162), (17, 162), (17, 166), (13, 166)]]
        self.assertTrue(obstacles.is_path_blocked(14,163))
        # self.assertTrue(obstacles.is_path_blocked(17,162))
        self.assertTrue(obstacles.is_path_blocked(16,165))
        self.assertTrue(obstacles.is_path_blocked(15,162))