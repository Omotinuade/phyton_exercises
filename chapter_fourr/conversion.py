import doctest
def celsius_to_fahrenheit(celsius_value):
    """This function to convert celcius to fahrenheit
    :param: celsius_value: float
    :return: float
    >>> celsius_to_fahrenheit(16)
    60.8
    """
    return celsius_value * 1.8 + 32.0


celsius_value = 16
print(celsius_to_fahrenheit(16))


def my_name(name):
    print("My name is %s" % name)


my_name("Aaliyah")
