# monte_carlo_integration.py
import random

def get_max_y(f, a, b, steps=1000):
    max_y = 0
    for i in range(steps):
        x = a + (b - a) * i / steps
        y = f(x)
        if y > max_y:
            max_y = y
    return max_y

def monte_carlo_integration(f, a, b, n_points):
    max_y = get_max_y(f, a, b)
    under_curve = 0
    points_under = []
    points_above = []

    for _ in range(n_points):   
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)

        if y <= f(x):
            under_curve += 1
            points_under.append((x, y))
        else:
            points_above.append((x, y))

    rect_area = (b - a) * max_y
    estimated_integral = rect_area * (under_curve / n_points)
    area_under = (under_curve / n_points) * rect_area
    area_above = rect_area - area_under
    
    return estimated_integral, area_under, area_above, points_under, points_above, max_y, rect_area
