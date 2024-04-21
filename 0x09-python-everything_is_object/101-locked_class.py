#!/usr/bin/python3
""" LockedClass
"""


class LockedClass:
    """Class tp prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init method"""
        pass
