class Bank:
    def __init__(self, loan_amount, interest_rate, loan_duration):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_duraion = loan_duration

    def calculator(loan_amount, interest_rate, loan_duration):
        interest_rate_decimal = interest_rate / 100.0
        num_payments = loan_duration * 12
        monthly_interest_rate = interest_rate_decimal / 12.0
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-num_payments))
        total_payment = monthly_payment * num_payments
        monthly_payment = round(monthly_payment, 2)
        total_payment = round(total_payment, 2)
        return monthly_payment, total_payment

    numbers_test_one = calculator(20000, 5, 10)
    print(numbers_test_one)
