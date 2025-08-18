> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# HW5: Biometric Fingerprint Processing

## Overview

This assignment is based on [this Nifty Assignment](http://nifty.stanford.edu/2024/servin-alonso-garcia-fingerprint/).

Welcome to the Biometric Fingerprint Processing assignment! In this project, you will learn how biometric fingerprint information is stored and used for authentication. You'll implement a fingerprint processing system that can read, store, display, and compare fingerprint data.

This assignment will help you gain hands-on experience with:
- Reading and processing data from files
- Working with 2D arrays in Python
- Creating and using classes with multiple methods
- Implementing comparison algorithms
- Building an incident response system for authentication

## Learning Objectives

By completing this assignment, you will:
1. Learn to read and store biometric data from files into 2D arrays
2. Build a `FingerPrint` class in Python to encapsulate fingerprint data
3. Implement comparison methods with statistical tolerance
4. Create an incident response system to handle failed authentication attempts

## Assignment Structure

The assignment is divided into three main parts:

### Part 1: File Processing and 2D Arrays
- Create a `fingerprint.py` file with a `FingerPrint` class
- Implement constructors and methods to handle fingerprint data
- Read fingerprint files and store data in 2D arrays

### Part 2: Incident Response Implementation
- Extend your program to handle authentication attempts
- Implement a system to track and limit failed attempts
- Add logic for granting or denying access

### Part 3: Statistical Analysis
- Implement statistical comparison between fingerprints
- Calculate match accuracy as a percentage
- Allow authentication based on a threshold match percentage

## Data
- We have a number of text files under the `data` folder.
- `Original.txt` will be the main fingerprint.
- `User1.txt`, `User2.txt` and so on will be fingerprints of different users (other than oringinal).
- `variation1.txt`, `variation2.txt` and so on are different variations of `Original.txt`, to be used for testing error threshold.
 
## Getting Started

### Required Files
1. `fingerprint.py` - Contains the `FingerPrint` class
2. `fileprocessor.py` - Contains the main application logic
3. `incidentresponse.py` - Contains the logic for the lockout handling
4. Sample fingerprint text files (included in the repository)

### FingerPrint Class Requirements

Your `FingerPrint` class should include:

#### Fields:
- `data`: a 2D list of single-character strings
- `name`: the fingerprint owner's name (str)
- `year`: the year it was registered (int)
- `rows`: number of rows in data (int)
- `cols`: number of columns in data (int)

#### Constructors:
- `__init__(self, filename: str)`: File constructor that reads fingerprint data from a file
- `__init__(self, data, name, year, rows, cols)`: Direct constructor that sets all fields

#### Methods:
- `get_number_of_pixels()`: Returns the total number of pixels (rows × columns)
- `__str__()`: Returns a string representation of the fingerprint
- `display_image()`: Prints the fingerprint image in text form
- `__eq__(other)`: Checks if two fingerprints are identical
- `match(other)`: Returns the accuracy percentage between two fingerprints

### Incident Response Requirements

Your `incidentresponse.py` file should include:

- An `authenticate` function that:
  - Accepts the original fingerprint, max allowed attempts, and error threshold
  - Loops to prompt for user fingerprint file names
  - Loads fingerprints using the `FingerPrint` class
  - Calculates match percentage
  - Grants access if match ≥ threshold
  - Increments attempt counter on failure
  - Locks system and exits after max failures

### File Processor Requirements

Your `fileprocessor.py` file should include:

1. Loading multiple fingerprint files
2. Setting up an original fingerprint for comparison
3. Setting a maximum number of authentication attempts
4. An interactive loop for authentication
5. Statistical comparison using an accuracy threshold

## Implementation Guide

### Part 1: Creating the FingerPrint Class

1. Create a file called `fingerprint.py`
2. Implement the `FingerPrint` class with all required fields, constructors, and methods
3. Ensure your file constructor can correctly read and parse fingerprint files
4. Implement a string representation that shows name, year, and pixel count
5. Create a method to display the fingerprint as a text image
6. Add a method to compare two fingerprints for exact matches

### Part 2: Building the File Processor

1. Create a file called `fileprocessor.py`
2. Load at least three different fingerprint files
3. Define a global variable for the original fingerprint
4. Set a maximum number of allowed authentication attempts
5. Implement a loop that:
  - Prompts the user for a fingerprint file
  - Loads the file using your `FingerPrint` class
  - Compares it to the original fingerprint
  - Grants or denies access based on the comparison
  - Tracks the number of failed attempts
  - Locks the system after too many failed attempts

### Part 3: Adding Statistical Analysis

1. Define an error threshold (e.g., 0.90 or 90%)
2. Implement a `match()` method in your `FingerPrint` class that:
  - Compares two fingerprints pixel by pixel
  - Calculates the percentage of matching pixels
  - Returns the accuracy as a decimal between 0 and 1
3. Update your authentication logic to:
  - Use the match percentage instead of exact matching
  - Grant access if the match percentage is above the threshold
  - Deny access otherwise

## Testing Your Implementation

To test your implementation:
1. Create several fingerprint files with varying levels of similarity
2. Run your `fileprocessor.py` program
3. Try authenticating with different fingerprint files
4. Observe how the system handles matches, near-matches, and non-matches
5. Test the incident response system by deliberately failing authentication multiple times

## Test Files

- `test_fileprocessor.py` should:
  - Patch `input()` to simulate user entries
  - Patch `authenticate()` to check if delegation is working
  - Include TODO comments for where to mock and assert

- `test_incidentresponse.py` should:
  - Patch `input()` and simulate various attempts
  - Test access granted when accuracy ≥ threshold
  - Test lockout when max attempts are exceeded
  - Include TODO comments for asserting access results


## Grading Rubric (Temporary)

Your assignment will be graded based on:
- Correct implementation of the `FingerPrint` class (30%)
- Proper file processing and 2D array handling (20%)
- Accurate fingerprint comparison logic (20%)
- Working incident response system (15%)
- Statistical analysis implementation (15%)

## Resources

- Sample fingerprint text files are provided in the repository
- Python documentation on file handling: [Python File Handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- Python documentation on classes: [Python Classes](https://docs.python.org/3/tutorial/classes.html)

Feel free to ask questions if anything is unclear. Good luck with your assignment!
