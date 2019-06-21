from math import factorial as f
from scipy import product as p


def probability(n, s, target):
    """
    ---------------------------------------------------------
    n: int      - number of dice
    s: int      - number of sides of a dice
    target: int - target scores
    ---------------------------------------------------------
    for more information visit this page:
    http://mathworld.wolfram.com/Dice.html
    """

    if 1 * n > target or target > s * n: return 0.0

    total_rolls, lucky_rolls = s**n, 0
    for k in range(((target - n) // s) + 1):
        a = (-1) ** k * f(n) / (f(k) * f(n - k))
        b = p([(target - s * k - i) / i for i in range(1, n)])
        lucky_rolls += a * b
    return round(lucky_rolls / total_rolls, 4)
