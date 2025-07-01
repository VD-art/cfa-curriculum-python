def future_value(pv, rate, n):
    """
    FV of single sum.
    pv: present value
    rate: interest rate per period (decimal, e.g., 0.05)
    n: number of periods
    """
    return pv * (1 + rate) ** n

def present_value(fv, rate, n):
    """
    PV of single sum.
    """
    return fv / (1 + rate) ** n

def future_value_annuity(payment, rate, n):
    """
    FV of ordinary annuity.
    """
    return payment * ((1 + rate) ** n - 1) / rate

def present_value_annuity(payment, rate, n):
    """
    PV of ordinary annuity.
    """
    return payment * (1 - 1 / (1 + rate) ** n) / rate

def present_value_uneven_cash_flows(cash_flows, rate):
    """
    PV of uneven cash flows.(NPV)
    cash_flows: list of tuples (cf, period)
    """
    pv = 0
    for cf, t in cash_flows:
        pv += cf / (1 + rate) ** t
    return pv
