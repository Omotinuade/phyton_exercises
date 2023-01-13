class CreditCard:
    def __init__(self, card_number: str):

        # self.card_type = None
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
        for i in range(len(self.card_number), 1, -2):
            number = int(i)
            odd_sum += number
        return odd_sum

    def even_sum_calculator(self):
        even_sum = 0
        for i in range(len(self.card_number) - 1, 1, -2):
            multiple = int(i) * 2
            if len(str(multiple)) == 2:
                even_sum = int(multiple[0]) + int(multiple[1])
            else:
                even_sum += multiple

        return even_sum

    def validate(self):
        if (self.odd_number_calculator() + self.even_sum_calculator()) % 10 == 0:
            print("Valid")
        else:
            print("Invalid")

    def card_length(self):
        card_length = len(self.card_number)

        return card_length


