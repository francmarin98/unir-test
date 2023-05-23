import app
import math

class InvalidPermissions(Exception):
    pass

class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y


     # Función que calcula la raíz cuadrada de un número
    def sqrt(self, x):
        self.check_types_one_parameter(x)
        if x <= 0:
            raise TypeError("The square root of a number less than or equal to 0 does not exist")
        
        return math.sqrt(x)


    # Función que calcula el logaritmo en base 10 de un número
    def log(self, x):
        self.check_types_one_parameter(x)
        if x <= 0:
            raise TypeError("The logarithm of a number less than or equal to 0 does not exist")
        
        return math.log10(x)


    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
        
    def check_types_one_parameter(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
