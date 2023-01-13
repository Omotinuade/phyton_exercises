from credit_card import CreditCard

card1 = CreditCard('5399831619690403')


def display():
    print('*' * 30, end=" ")
    print('**Credit Card Type:', card1.card_type_validator)
    print('**Credit Card Number:', card1.card_number)
    print('**Credit Card Digit Length:', card1.card_length)
    print('**Credit Card Validity Status:', card1.validate)
    print('*' * 30, end=" ")


print(display())
