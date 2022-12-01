import customtkinter
import math

class Calculator:
    """Calculator Core"""

    def adiction(self, a, b):
        """Addition"""
        return a + b
    
    def subtraction(self, a, b):
        """Subtraction"""
        return a - b
    
    def multiplication(self, a, b):
        """Multiplication"""
        return a * b
    
    def division(self, a, b):
        """Division"""
        if b == 0:
            return "Error: Division by zero"
        return a / b
    
    def square_root(self, a):
        """Square root"""
        return math.sqrt(a)
    
    def potenciation(self, num, pot):
        """Square"""
        return num ** pot
