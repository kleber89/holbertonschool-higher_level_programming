#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry 
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Representa un rectángulo con atributos de ancho y alto.
    """
    def __init__(self, width, height):
        """
        Inicializa un objeto Rectangle.

        Args:
            width (int): El ancho del rectángulo.
            height (int): La altura del rectángulo.

        Raises:
            TypeError: Si width o height no es un entero.
            ValueError: Si width o height no son estrictamente positivos.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self.height = height
