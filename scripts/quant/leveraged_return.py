def leveraged_return(unleveraged_return, leverage_factor):
    """
    Calculate leveraged return.
    
    unleveraged_return: return without leverage (decimal, e.g. 0.10 for 10%)
    leverage_factor: total investment / own equity (e.g., 1.5 means 50% leverage)
    """
    return unleveraged_return * leverage_factor
