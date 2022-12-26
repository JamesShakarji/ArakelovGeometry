# Define the surface as a 2D grid
surface = np.array([[(x, y) for x in np.linspace(-1, 1, 10)] for y in np.linspace(-1, 1, 10)])

# Define the height function as a Gaussian function
def height_function(x, y):
    return np.exp(-x**2 - y**2)

# Create an instance of the ArakelovGeometry class
arakelov = ArakelovGeometry(surface, height_function)

# Define the first curve as a circle with radius 0.5 centered at (0, 0)
curve_1 = np.array([(0.5*np.cos(theta), 0.5*np.sin(theta)) for theta in np.linspace(0, 2*np.pi, 100)])

# Define the second curve as a line with slope 1 and y-intercept -1
curve_2 = np.array([(x, x-1) for x in np.linspace(-1, 1, 100)])

# Compute the intersection points of the two curves
intersection_points = arakelov.intersection(curve_1, curve_2)
print(intersection_points)

# Compute the distance between two points on the surface
point_1 = (0, 0)
point_2 = (1, 1)
distance = arakelov.distance(point_1, point_2)
print(distance)
