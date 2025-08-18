# IncidentResponse.py

import sys
import fileprocessor

# Module‐level counter for failed attempts
_failed_attempts = 0

def authenticate(fp):
    """
    Given a FingerPrint `fp`, compare it against the global original.
    Return True if access is granted, False if denied (but not yet locked out).
    Call handle_lockout() once max_tries is exceeded.
    """
    global _failed_attempts

    # TODO: Part 1 – Prevent users from exceeding max_tries
    #   If it exceeds max tries call handle_lockout()

    # TODO: Part 2 – Exact‐match comparison
    #   See if the fingerprint matches exactly with the original.

    # TODO: Part 3 – Threshold comparison
    #   * Compute accuracy using fp.match()
    #   * If accuracy is satisfactory, return True

    # TODO: Part 4 – Track and report failures
    #   * Increment _failed_attempts
    #   * Print remaining tries
    #   * If now >= max_tries, call handle_lockout()

    return False

def handle_lockout():
    """
    Called when maximum failed attempts have been reached.
    Should notify the user and exit or raise an exception.
    """
    # TODO: Print lockout message and exit the program
    pass
