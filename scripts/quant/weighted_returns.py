import numpy_financial as npf

def money_weighted_return(cash_flows):
    """
    Calculate money-weighted return = IRR of cash flows.
    cash_flows: list of amounts over time (negative for outflows, positive for inflows).
    """
    return npf.irr(cash_flows)

def time_weighted_return(sub_period_returns):
    """
    Calculate time-weighted return = geometric mean of sub-period returns.
    sub_period_returns: list of decimal returns for each sub-period.
    """
    product = 1
    for r in sub_period_returns:
        product *= (1 + r)
    return product**(1/len(sub_period_returns)) - 1
