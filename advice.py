def financial_advice(total):

    if total == 0:
        return "Start tracking expenses to understand spending habits."

    if total < 3000:
        return "Excellent! Your spending is under control."

    if total < 7000:
        return "Moderate spending detected. Consider saving 20%."

    if total < 12000:
        return "Spending is increasing. Set a monthly budget."

    return "High spending detected! Reduce unnecessary purchases."