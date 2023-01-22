class CreditCard:
    def __init__(self, card_number: str):
        if not (13 <= len(card_number) <= 16):
            raise ValueError("Card number must have between 13 and 16 digits")
        self.card_number = card_number

    def card_type_validator(self):
        card_type = ''
        if self.card_number.startswith('4'):
            card_type = 'Visa card'
        elif self.card_number.startswith('5'):
            card_type = 'Master card'
        elif self.card_number.startswith('37'):
            card_type = 'American visa card'
        elif self.card_number.startswith('6'):
            card_type = 'Discover card'

        return card_type

    def odd_number_calculator(self):
        odd_sum = 0
        reversed_number = self.card_number[::-1]
        # print(reversed_number)
        for i, number in enumerate(reversed_number):
            if i % 2 == 0:
                odd_sum += int(number)
        return odd_sum

    def even_sum_calculator(self):
        even_sum = 0
        reversed_number = self.card_number[::-1]
        for i, number in enumerate(reversed_number):
            if i % 2 == 1:
                product = 2 * int(number)
                product_str = str(product)
                if len(product_str) == 1:
                    even_sum += product
                else:
                    even_sum += 1 + product % 10

        return even_sum

    def validate(self):
        if (self.odd_number_calculator() + self.even_sum_calculator()) % 10 == 0:
            return "Valid"
        else:
            return "Invalid"

    def card_length(self):
        card_length = len(self.card_number)

        return card_length

    def display(self):
        print('*' * 50)
        print()
        print('**Credit Card Type:', self.card_type_validator())
        print('**Credit Card Number:', self.card_number)
        print('**Credit Card Digit Length:', self.card_length())
        print('**Credit Card Validity Status:', self.validate())
        print()
        print('*' * 50, end=" ")




