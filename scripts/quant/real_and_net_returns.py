def gross_return(ending_value, beginning_value):
    """
    Calculate gross return (before fees and taxes).
    """
    return (ending_value - beginning_value) / beginning_value

def net_return(gross_return, fees=0, taxes=0):
    """
    Calculate net return after subtracting fees and taxes (both as decimal fractions).
    """
    return gross_return * (1 - fees) * (1 - taxes)

def real_return(nominal_return, inflation_rate):
    """
    Calculate real return adjusted for inflation.
    """
    return (1 + nominal_return) / (1 + inflation_rate) - 1
