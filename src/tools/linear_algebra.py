import math
from typing import List


Vector = List[float]


def add (v: Vector, w: Vector) -> Vector:
    if len(v) != len(w):
        raise RuntimeError("Vector must be of the same length")
    return [v_i + w_i for v_i, w_i in zip(v, w)]
