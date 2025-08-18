from fingerprint import FingerPrint

# Global configuration
original = None       # Original Finger Print - Will be initialized in main()
max_tries = 15         # Maximum failed attempts allowed, assign your own value.
err_thresh = 0.50     # Minimum matching fraction to grant access, once again use your own value.

def load_fingerprint(filename: str) -> FingerPrint:
    """Read any fingerprint.txt file and return a FingerPrint object."""
    # TODO: Create and return a new FingerPrint object using the filename
    pass

def main():
    """Entry point for the interactive application."""
    global original

    # TODO: Initialize the original fingerprint from a file
    # Example: original = load_fingerprint("Original.txt")

    # TODO: Print information about the original fingerprint
    #   - Print name, year, rows, cols
    #   - Print the string representation
    #   - Print the number of pixels
    #   - Display the image

    # TODO: Authentication loop
    #   - Prompt user for fingerprint file
    #   - Load fingerprint
    #   - Call IncidentResponse.authenticate(fp)
    #       * If True: inform access granted and break
    #       * If False but not locked out: inform access denied and continue
    #       * If locked out: IncidentResponse.handle_lockout() will exit

if __name__ == '__main__':
    main()