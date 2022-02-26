from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item that is either a gem or a rock. 
    
    The responsibility of an Artifact is to provide a value depending on if it is a gem or rock.

    Attributes:
        points (int): A value of the Artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        
    def get_points(self):
        """Gets the Artifact's points.
        
        Returns:
            points: The point value of the Artifact.
        """
        return self._points
    
    def set_points(self, points):
        """Assigns the points of the Artifact.
        
        Args:
            points (int): The given points.
        """
        self._points = points
