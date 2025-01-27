import random
def random_bias(bias: float) -> bool:
    """
    Given a probability bias between 0 and 1, return a boolean value
    based on the probability of the bias.
    """
    return random.random() < bias