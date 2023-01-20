#!/usr/bin/python3   
"""

This module is composed by a function that adds two numbers

"""

def add_integer(a, b = 98):                                                                    
    """ Function that adds two integer or float numbers

    Arguments passed:
        a: first number
        b: second number

    Returns:
        The sum of the two numbers given

    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    
    """                                                                  
                                                                                               
     # Checking the user input type                                                            
    if type(a & b) not in [int, float]:                                                           
        raise TypeError(" must be an integer or b must be an integer")                         
                                                                                               
    return int(a) + int(b)  
