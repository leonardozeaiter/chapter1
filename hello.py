import math
from mymath import math1 as m

class Person:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Person(id={self.id}, name={self.name})"
    
    def add(self, a: int, b: int) -> int:
        """
        Adds two integers and return the sum as integer
        
        :param self: the entity
        :param a: first integer
        :type a: int
        :param b: second integer
        :type b: int
        :return: Returns the sum of a and b
        :rtype: int
        """
        return a + b
    

leo = Person(1, "Leonardo Zeaiter")

print(leo.add(1,2))

print(m.subtract(6,5))