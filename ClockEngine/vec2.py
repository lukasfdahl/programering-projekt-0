import math

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def add(vec_a: tuple[float, float], vec_b: tuple[float, float]) -> tuple[float, float]:
    return (vec_a[0] + vec_b[0], vec_a[1] + vec_b[1])


def subtract(vec_a: tuple[float, float], vec_b: tuple[float, float]) -> tuple[float, float]:
    return (vec_a[0] - vec_b[0], vec_a[1] - vec_b[1])


def multiply(vec_a: tuple[float, float], vec_b: tuple[float, float]) -> tuple[float, float]:
    return (vec_a[0] * vec_b[0], vec_a[1] * vec_b[1])
def multiply(vec_a: tuple[float, float], number : float) -> tuple[float, float]:
    return (vec_a[0] * number, vec_a[1] * number)


def divide(vec_a: tuple[float, float], vec_b: tuple[float, float]) -> tuple[float, float]:
    return (vec_a[0] / vec_b[0], vec_a[1] / vec_b[1])
def divide(vec_a: tuple[float, float], number : float) -> tuple[float, float]:
    return (vec_a[0] / number, vec_a[1] / number)

def distance(vec_a: tuple[float, float], vec_b : tuple[float, float]) -> float:
    return math.sqrt((vec_a[0] - vec_b[0]) ** 2 + (vec_a[1] - vec_b[1]) ** 2)

def rotate_point(pivot_point: tuple[float, float],angle : float, target_point : tuple[float, float]) -> tuple[float, float]:
    s = math.sin(angle)
    c = math.cos(angle)
    new_target_point = list(target_point[:])
    new_target_point[0] -= pivot_point[0]
    new_target_point[1] -= pivot_point[1]
    
    xnew = new_target_point[0] * c - new_target_point[1] * s
    ynew = new_target_point[0] * s + new_target_point[1] * c

    new_target_point[0] = xnew + pivot_point[0]
    new_target_point[1] = ynew + pivot_point[1]

    return tuple(new_target_point)

def rotate_vec(vec : tuple[float, float], rot : float) -> tuple[float, float]:
    cs = math.cos(rot)
    sn = math.sin(rot)

    x = vec[0] * cs - vec[1] * sn
    y = vec[0] * sn + vec[1] * cs
    return (x, y)

def negate_y(vec : tuple[float, float]):
    return (vec[0], -vec[1])

def angle(vec_a : tuple[float, float], vec_b : tuple[float, float]) -> float:
    if (vec_a[0] == 0 and vec_a[1] == 0) or (vec_b[0] == 0 and vec_b[1] == 0):
        return 0
    return math.acos((vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]) / (math.sqrt(vec_a[0] ** 2 + vec_a[1] ** 2) * math.sqrt(vec_b[0] ** 2 + vec_b[1] ** 2)))

def angle_clockwise(vec_a : tuple[float, float], vec_b : tuple[float, float]) -> float:
    dot = vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]
    det = vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0]
    return -math.atan2(det, dot)