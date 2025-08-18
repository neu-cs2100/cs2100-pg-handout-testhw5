#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `FingerPrint` class as described in README.md
"""

class FingerPrint:
    def __init__(self, *args):
        """
        Two constructors:
        - __init__(self, filename: str)
        - __init__(self, data, name, year, rows, cols)
        Use argument count or types to distinguish.
        """
        # File constructor
        if len(args) == 1 and isinstance(args[0], str):
            filename = args[0]
            # TODO: Open the file and read it line by line
            # TODO: Extract name from first line
            # TODO: Extract year from second line (convert to int)
            # TODO: Extract rows from third line (convert to int)
            # TODO: Extract cols from fourth line (convert to int)
            # TODO: Read the next 'rows' lines and split each into a list of characters
            # TODO: Store the resulting 2D list in self.data
            pass
        
        # Direct constructor
        elif len(args) == 5:
            # TODO: Assign the parameters to the corresponding instance variables
            pass
        
        else:
            raise ValueError("Invalid constructor arguments")

    def get_number_of_pixels(self):
        """Return total pixels (rows * cols)."""
        # TODO: Return the product of rows and cols
        pass

    def __str__(self):
        """Return summary string."""
        # TODO: Return formatted string with name, year, and pixel count
        # Format: "Fingerprint for: <name>. Year registered: <year>. Number of Pixels: <pixels>"
        pass

    def display_image(self):
        """Print each row of the fingerprint grid."""
        # TODO: Iterate through the data 2D array
        # TODO: Print each character in a row without spaces
        # TODO: Add a newline after each row
        pass

    def __eq__(self, other):
        """Exact equality: name, year, dims, all pixels."""
        # TODO: Check if name, year, rows, and cols are equal
        # TODO: Check if all pixels in the data arrays match
        # TODO: Return True only if everything matches
        pass

    def match(self, other):
        """Return fraction of pixels matching (0.00 - 1.00)."""
        # TODO: Count how many pixels match between self and other
        # TODO: Divide by total number of pixels to get match percentage
        # TODO: Return the result as a float between 0.00 and 1.00
        pass
    
    # Getters and setters (optional but could be useful)
    def get_data(self):
        return self.data
    
    def get_name(self):
        return self.name
    
    def get_year(self):
        return self.year
    
    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols