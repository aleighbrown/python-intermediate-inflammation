"""Tests for the Patient model."""

import numpy as np
import pytest
from inflammation.models import Patient


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name

def test_patient_inflamation():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert isinstance(p.observations,list)

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Alice'
    p = Doctor(name=name)

    assert p.name == name

@pytest.mark.parametrize(
    "test, raises",
    [
        (
                [Patient('alice'),Patient('alice')],
                None,
        ),
        (
                [Patient('alice'),'a'],
                TypeError,
        )
    ])
def test_patient_normalise(test, raises):
    """Test that you can create a Doctor with list of patients"""
    from inflammation.models import Doctor, Patient

    if raises:
        with pytest.raises(raises):
            p = Doctor(name='alice', patients=test)
    else:
        p = Doctor(name='alice', patients=test)
