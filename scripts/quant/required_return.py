def calculate_required_return(real_risk_free_rate, inflation_premium=0, default_risk_premium=0, 
                              liquidity_premium=0, maturity_premium=0):
    """
    Calculate required return as the sum of components.
    
    Parameters:
    - real_risk_free_rate: base rate (decimal, e.g. 0.02)
    - inflation_premium: expected inflation (decimal)
    - default_risk_premium: extra for default risk
    - liquidity_premium: extra for illiquidity
    - maturity_premium: extra for maturity risk

    Returns:
    - required return (decimal)
    """
    return (real_risk_free_rate + inflation_premium + default_risk_premium 
            + liquidity_premium + maturity_premium)
