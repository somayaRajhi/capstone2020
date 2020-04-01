"""
Errors for job-queue class
"""


class NoJobsAvailableException(Exception):
    """
    Thrown exception for an empty unassigned_jobs_list.
    """


class UnassignInvalidDataException(ValueError):
    """
    Thrown exception for assigning an invalid job.
    """
