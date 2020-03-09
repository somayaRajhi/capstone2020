"""
Errors for retriving a docket using regulation.gov api
"""


class IncorrectApiKey(Exception):
    """
    Thrown exception for an incorrectly entered reg gov api key
    """


class ExceedCallLimit(Exception):
    """
    Thrown exception for overuse of a reg gov api key
    """


class BadDocketID(Exception):
    """
    Thrown exception for a docket id that does not exist
    """


class IncorrectIDPattern(Exception):
    """
    Thrown exception for a incorrect docket id pattern
    """
