def arithmetic_mean(returns):
    """
    Calculate arithmetic mean of a list of returns.
    """
    return sum(returns) / len(returns)

def geometric_mean(returns):
    """
    Calculate geometric mean of a list of returns.
    Returns must be in decimal form, e.g., 0.05 for 5%.
    """
    product = 1
    for r in returns:
        product *= (1 + r)
    return product**(1/len(returns)) - 1

def harmonic_mean(values):
    """
    Calculate harmonic mean of a list of numbers.
    """
    return len(values) / sum(1/v for v in values)
