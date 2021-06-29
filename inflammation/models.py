"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    :param data: numpy array where rows are patients and columns are days
    :returns: mean value across patients measurement per day
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    :param data: numpy array where rows are patients and columns are days
    :returns: an array of max value across patients measurement per day
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    :param data: numpy array where rows are patients and columns are days
    :returns: an array of min value across patients measurement per day
    """
    return np.min(data, axis=0)


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
