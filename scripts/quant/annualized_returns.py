import math

def annualize_return(return_per_period, periods_per_year):
    """
    Annualize return given return per period and number of periods per year.
    """
    return (1 + return_per_period)**periods_per_year - 1

def effective_annual_rate(nominal_rate, compounding_periods):
    """
    Calculate EAR given nominal annual rate and number of compounding periods per year.
    """
    return (1 + nominal_rate/compounding_periods)**compounding_periods - 1

def continuous_compounding_rate(discrete_rate):
    """
    Convert discrete annual rate to continuously compounded rate.
    """
    return math.log(1 + discrete_rate)

def discrete_rate_from_continuous(continuous_rate):
    """
    Convert continuously compounded rate back to discrete annual rate.
    """
    return math.exp(continuous_rate) - 1
