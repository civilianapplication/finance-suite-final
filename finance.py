CORP_TAX = 0.25

DIV_BASIC = 0.0875
DIV_HIGH = 0.3375

BASIC_LIMIT = 37700
HIGH_LIMIT = 125140

PENSION_ALLOWANCE = 60000


def breakdown(transactions):
    income = sum(t[2] for t in transactions if t[0] == "income")
    expenses = sum(t[2] for t in transactions if t[0] == "expense")
    dividends = sum(t[2] for t in transactions if t[0] == "dividend")

    return income, expenses, dividends


def profit(income, expenses, salary, pension):
    return income - expenses - salary - pension


def corp_tax_amount(p):
    return max(0, p) * CORP_TAX


def retained(p, tax, dividends):
    return p - tax - dividends


def safe_withdrawal(retained):
    return max(0, retained * 0.8)


def pension_headroom(current):
    return max(0, PENSION_ALLOWANCE - current)
