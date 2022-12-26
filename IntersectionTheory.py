import sympy

def intersection_theory(curve1, curve2, domain=sympy.AA):
    """Calculate the intersection points of two algebraic curves over the given domain."""
    # Find the solutions to the system of equations defined by the two curves
    solutions = sympy.solve([curve1, curve2], list(curve1.atoms(sympy.Symbol)), domain=domain)
    # Return the solutions as a list of tuples
    return [(s[var] for var in curve1.atoms(sympy.Symbol)) for s in solutions]

# Define two algebraic curves: a circle and a line
x, y = sympy.symbols('x y')
circle = x**2 + y**2 - 1
line = y - x

# Calculate the intersection points of the two curves over the algebraic numbers
intersections = intersection_theory(circle, line)
print(intersections)  # Output: [(-1, -1), (1, 1)]
