"""
a set of custom errors specific to the regulations.gov api
"""


class InvalidApiKeyException(Exception):
    pass


class RateLimitException(Exception):
    pass


class BadDocumentIDException(Exception):
    pass
