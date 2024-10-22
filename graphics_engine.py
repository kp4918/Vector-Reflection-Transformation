 Install python
# python -m venv graphics-env
# source graphics-env/bin/activate  # On Windows use: graphics-env\Scripts\activate
# pip install pygame

# Create a Basic Pygame Window
import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Graphics Engine")

# Implement Linear Transformations
def translate(point, tx, ty):
    """Translate a point by (tx, ty)."""
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    point_homogeneous = np.array([point[0], point[1], 1])
    translated_point = translation_matrix @ point_homogeneous
    return translated_point[:2]

def scale(point, sx, sy):
    """Scale a point by (sx, sy)."""
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    point_homogeneous = np.array([point[0], point[1], 1])
    scaled_point = scaling_matrix @ point_homogeneous
    return scaled_point[:2]

def rotate(point, angle):
    """Rotate a point by angle (in radians)."""
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
    point_homogeneous = np.array([point[0], point[1], 1])
    rotated_point = rotation_matrix @ point_homogeneous
    return rotated_point[:2]

# Draw Shapes and Apply Transformations
def draw_shape(screen, shape, color):
    """Draw a shape on the screen."""
    pygame.draw.polygon(screen, color, shape)

def apply_transformations(shape, tx, ty, sx, sy, angle):
    """Apply translation, scaling, and rotation to a shape."""
    transformed_shape = [translate(vertex, tx, ty) for vertex in shape]
    transformed_shape = [scale(vertex, sx, sy) for vertex in transformed_shape]
    transformed_shape = [rotate(vertex, angle) for vertex in transformed_shape]
    return transformed_shape

def main():
    # Original shape (triangle)
    shape = np.array([[100, 100], [150, 50], [200, 100]])  # Triangle vertices
    shape_color = (0, 255, 0)  # Green color
    original_color = (255, 0, 0)  # Red color for original shape

    # Transformation parameters
    tx, ty = 100, 50  # Translation offsets
    sx, sy = 1.5, 1.5  # Scaling factors
    angle = np.pi / 4  # Rotation angle in radians (45 degrees)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with white
        screen.fill((255, 255, 255))

        # Apply transformations to the shape
        transformed_shape = apply_transformations(shape, tx, ty, sx, sy, angle)

        # Draw the original shape (in red) and the transformed shape (in green)
        draw_shape(screen, shape, original_color)  # Original shape
        draw_shape(screen, transformed_shape, shape_color)  # Transformed shape

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

