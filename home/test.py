from typing import Any


class MaxValueValidator:
    def __init__(self, max_value) :
        self.max_value = max_value
        
    
    def __call__(self, value):
        if value > self.max_value:
            raise ValueError(f' value must be less than or equal to {self.max_value}')
        


class MinValueValidator:
    def __init__(self, min_value) :
        self.min_value = min_value
        
    
    def __call__(self, value):
        if value < self.min_value:
            raise ValueError(f' value must be greater than or equal to {self.min_value}')
        

max_validator = MaxValueValidator()
min_validator = MinValueValidator()

