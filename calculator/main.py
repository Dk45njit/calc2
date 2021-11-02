""" This is the  increment function"""
number_types = (int, float, complex)
""" This is the  data type function"""
class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def validate_args(value_x, value_y):
        """ This is to validate the arguments"""
        if not isinstance(value_x, number_types) and not isinstance(value_y, number_types):
            raise ValueError
    def add(self, value_x, value_y):
        """ addition of number from result"""
        self.validate_args(value_x, value_y)
        return value_x + value_y
    def sub(self, value_x, value_y):
        """ subtract number from result"""
        self.validate_args(value_x, value_y)
        return value_x - value_y
    def multiply(self, value_x, value_y):
        """ multiply two Numbers and store the result"""
        self.validate_args(value_x, value_y)
        return value_x * value_y
    def div(self, value_x, value_y):
        """ divide two Numbers and store the result"""
        self.validate_args(value_x, value_y)
        return value_x / value_y
