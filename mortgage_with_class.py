"""
DOCSTRING
Mortgage calculator
Calculate month payments for mortgage credit with fixed sum, credit term, given interest rate
and the number of payments to equal N. Also count, how much the user will pay in total.

Ипотечный Калькулятор
Вычислите ежемесячные платежи для ипотечного кредита с фиксированной суммой, сроком кредита, заданной процентой ставкой
и количеством перерасчета n. Также посчитайте, сколько всего в итоге заплатит пользователь.
"""


class Mortgage:

    def __init__(self, summ, term, percent, settlement_period=12):
        self.summ = summ
        self.term = term
        self.percent = percent
        self.settlement_period = settlement_period

    def __str__(self):
        return f'You change mortgage with sum = {self.summ}$, term = {self.term} years, interest rate = {self.percent}'\
               f'% and settlement period = {self.settlement_period} times in years'

    def simple_mortgage(self):
        overpayment = self.summ * self.term * self.percent / 100
        total_sum = overpayment + self.summ
        print(f'Total sum of mortgage is {total_sum}. Overpayment is {overpayment}')
        month_payment = round((total_sum / (self.term * 12)), 2)
        month_interest = round((overpayment / (self.term * 12)), 2)
        print(f'Your month payment is {month_payment}, of which {month_interest} is interest and '
              f'{round((month_payment - month_interest), 2)} is the mortgage body')
        return ''

    def difficult_annuity_mortgage(self):
        interest = self.percent / 100 / 12
        payment = self.summ * (interest * (1 + interest)**(self.term * 12)) / ((1 + interest)**(self.term * 12) - 1)
        total_payment = payment * self.term * 12
        overpayment = total_payment - self.summ
        num_payment = 0
        change_sum = self.summ
        for month in range(self.term * 12):
            num_payment += 1
            percent = change_sum * interest
            body_mortgage = payment - percent
            already_paid = payment * num_payment
            change_sum -= body_mortgage
            print(f'{num_payment} month - the payment is {round(payment, 2)} of which {round(percent, 2)} is the '
                  f'interest and {round(body_mortgage, 2)} is the mortgage body. Already paid:{round(already_paid, 2)}')
        print(f'Overpayment is {round(overpayment, 2)}')
        return ''

    def difficult_differentiated_mortgage(self):
        month_interest = self.percent / 12
        num_payment = 0
        total_payment = 0
        change_sum = self.summ
        for month in range(self.term * 12):
            num_payment += 1
            percent = round((change_sum * month_interest / 100), 2)
            body_mortgage = round((self.summ / (self.term * 12)), 2)
            payment = round((percent + body_mortgage), 2)
            total_payment += payment
            change_sum -= body_mortgage
            print(f'{num_payment} month - the payment is {payment} of which {percent} is the interest and '
                  f'{body_mortgage} is the mortgage body. Already paid: {round(total_payment, 2)}')
        print(f'Overpayment is {round((total_payment - self.summ), 2)}')
        return ''


my_sum = int(input("How much money do you need?  "))
my_term = int(input("How long do you need (years)?  "))
my_interest = int(input("How interest rate is set by the bank? "))
change = input('What mortgage do you want calculate? simple(s), annuity(a) or differentiated(d)?')
mortgage = Mortgage(my_sum, my_term, my_interest)
if change == 'simple' or change == 's':
    print(mortgage.simple_mortgage())
elif change == 'annuity' or change == 'a':
    print(mortgage.difficult_annuity_mortgage())
elif change == 'differentiated' or change == 'd':
    print(mortgage.difficult_differentiated_mortgage())
else:
    print('SIMPLE')
    print(mortgage.simple_mortgage())
    print('ANNUITY')
    print(mortgage.difficult_annuity_mortgage())
    print('DIFFERENTIATED')
    print(mortgage.difficult_differentiated_mortgage())
