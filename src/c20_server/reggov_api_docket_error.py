"""
Errors for retriving a docket using regulation.gov api
"""

class IncorrectApiKey(Exception):
    pass


class ExceedCallLimit(Exception):
    pass


class BadDocketID(Exception):
    pass


class IncorrectIDPattern(Exception):
    pass