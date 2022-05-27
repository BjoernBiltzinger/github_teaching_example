import numpy as np


class Student:
    """
    Handle a student for administration
    """
    def __init__(self, name, age, schoolclass):
        self._name = name
        self._age = age
        self._schoolclass = schoolclass

    def summary(self):
        """
        :return: String summary of student
        """
        return (f"Student {self._name} is {self._age} years old"
                f"and is in class {self._schoolclass}")

    def passed(self):
        """
        This student passed a class so he will be in the next one
        """
        self._schoolclass += 1

    def birthday(self):
        """
        This student got one year older
        """
        self._age += 1
