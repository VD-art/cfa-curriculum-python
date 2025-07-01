def calculate_required_return_components(real_risk_free_rate, inflation_premium=0, default_risk_premium=0, 
                                         liquidity_premium=0, maturity_premium=0):
    """
    Calculate required return and return all components.

    Returns:
    - A dict with each component and total required return
    """
    required = (real_risk_free_rate + inflation_premium + default_risk_premium 
                + liquidity_premium + maturity_premium)
    
    return {
        'real_risk_free_rate': real_risk_free_rate,
        'inflation_premium': inflation_premium,
        'default_risk_premium': default_risk_premium,
        'liquidity_premium': liquidity_premium,
        'maturity_premium': maturity_premium,
        'required_return': required
    }
