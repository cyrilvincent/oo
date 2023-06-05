from typing import List, Tuple

def min_max(l: List[float]) -> Tuple[float, float]:
    min = l[0]
    max = l[0]
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

toto, max = min_max([1, 2, 3])
print(toto, max)