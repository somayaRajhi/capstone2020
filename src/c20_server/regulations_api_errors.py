"""
a set of custom errors specific to the regulations.gov api
"""


class IncorrectApiKey(Exception):
    pass


class ThousandCalls(Exception):
    pass


class BadID(Exception):
    pass
