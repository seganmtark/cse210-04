from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item that is either a gem or a rock. 
    
    The responsibility of an Artifact is to provide a value depending on if it is a gem or rock.

    Attributes:
        points (int): A value of the Artifact.
    """
    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._get_point = 1
    
    def set_points(self, get_point):
        """Set the points for artifacts."""
        self._get_point = get_point

    def get_earn_point(self):
        """Gets the points value of Artifact."""
        return self._get_point
