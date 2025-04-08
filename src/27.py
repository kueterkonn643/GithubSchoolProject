import math

def calculate_area(shape, dimensions):
    """
    Calculate the area of a shape.
    
    Parameters:
        shape (str): The type of shape ('rectangle', 'circle', 'triangle').
        dimensions (tuple): A tuple containing the dimensions of the shape in the order [length, width].
        
    Returns:
        float: The area of the shape.
    """
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions[0]
        area = math.pi * (radius ** 2)
        return area
    elif shape == "triangle":
        base, height = dimensions
        area = 0.5 * base * height
        return area
    else:
        raise ValueError("Unsupported shape type")

# Example usage:
rect_length = 10
rect_width = 5

circle_radius = 3
area_circle = calculate_area("circle", (circle_radius, circle_radius))

triangle_base = 6
triangle_height = 4
area_triangle = calculate_area("triangle", (triangle_base, triangle_height))
