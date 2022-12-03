'''
Example 1
even_numbers = [i for i in range(0,100) if i % 2 == 0]
print(even_numbers)
'''

transactions = [100,200,300,150,80]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07

def get_price_tax_service(bill):
    return bill*(1 + TAX_RATE + SERVICE_CHARGE)

final_prices = [get_price_tax_service(bill) for bill in transactions]
print(final_prices)
