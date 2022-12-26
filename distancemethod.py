import numpy as np
from scipy.spatial.distance import euclidean

#You may use this prompt to understand the implementation of the two other files in this repo


class ArakelovGeometry:
    def __init__(self, surface, height_function):
        self.surface = surface
        self.height_function = height_function
    
    def intersection(self, curve_1, curve_2):
        """Computes the intersection of two curves on the surface."""
        # TODO: Implement the intersection computation
        pass
    
    def distance(self, point_1, point_2):
        """Computes the distance between two points on the surface."""
        # Extract the x and y coordinates of the points
        x1, y1 = point_1
        x2, y2 = point_2
        
        # Compute the Euclidean distance between the points on the surface
        distance = euclidean((x1, y1, self.height_function(x1, y1)), (x2, y2, self.height_function(x2, y2)))
        
        return distance

# Define the surface as a 2D grid
surface = np.array([[(x, y) for x in np.linspace(-1, 1, 10)] for y in np.linspace(-1, 1, 10)])

# Define the height function as a Gaussian function
def height_function(x, y):
    return np.exp(-x**2 - y**2)

# Create an instance of the ArakelovGeometry class
arakelov = ArakelovGeometry(surface, height_function)

# Define two points on the surface
point_1 =
