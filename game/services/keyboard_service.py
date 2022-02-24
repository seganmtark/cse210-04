import pyray
from game.shared.point import Point


class KeyboardService:
    """This class will detect and react to the player's keyboard input.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Initiates the variables to be used in KeyboardService
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Moves the player left and right based upon the keyboard input.

        Returns:
            Point: The selected direction.
        """
        dx = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        


        direction = Point(dx, 0)
        direction = direction.scale(self._cell_size)
        
        return direction