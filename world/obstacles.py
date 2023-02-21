import random
# from robot import my_obstacles
min_y, max_y = -200, 200
min_x, max_x = -100, 100
my_obstacles = []
def assign_obstacles(obstacles):
    global my_obstacles
    my_obstacles = obstacles

def is_position_blocked(x,y):
    """Function returns True if position (x,y) falls inside an obstacle.
    Args:
        x ([int]): The x coordinates
        y ([int]): The y coordinates 
    """

    for i in range(len(my_obstacles)):
        if x in range(my_obstacles[i][0][0], my_obstacles[i][2][0]) and y in range(my_obstacles[i][0][1], my_obstacles[i][2][1]):
            return True
    return False
    
def is_path_blocked(x1,y1):
    """Function returns True if there is an obstacle in the line between
       the coordinates (x1, y1) and (x2, y2)
    """

    for i in range(len(my_obstacles)):
        return is_position_blocked(x1+i,y1+i)
   
   
def get_obstacles():
    """Function returns an obstacle
    """ 
    #Random positions to place obstacles
    my_range = random.randint(0,10)
    obstacles = []
    for i in range(my_range):
        x = random.randint(min_x, max_x)
        y = random.randint(min_y, max_y)
        obst = [] 
        obst.append((x,y))
        obst.append((x+4,y))
        obst.append((x+4,y+4))
        obst.append((x,y+4))
        obstacles.append(obst)
    return obstacles

