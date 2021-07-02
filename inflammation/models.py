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

def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflamation array should be 2-dimensional')
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

def attach_names(data,names):
    """Create datastructure containing patient records.

    :param data: 2D array of inflammation data
    :param name: a list of strings which contain patient names

    :type data: ndarray
    :type name: list
    """
    assert len(data) == len(names)
    output = []

    for data_row, name in zip(data, names):
        output.append({'name': name,
                       'data': data_row})

    return output

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient:
    def __init__(self, name, observations=None):
        self.name = name

        if observations is None:
            self.observations = []

        else:
            self.observations = observations

    def add_observation(self, obs):
        self.observations.append(obs)

class Doctor(Person):
    def __init__(self, name, patients=None):
        super().__init__(name)
        if patients is None:
            patients = []
        if len(patients) > 0 and not all(isinstance(x, Patient) for x in patients):
            raise TypeError('patients needs to be a list of Patients')
        self.patients = patients





# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
