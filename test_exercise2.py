#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Anne Simon', 'Grant Wheeler'
__email__ = "anne.simon@mail.utoronto.ca", "grant.wheeler@mail.utoronto.ca"
__copyright__ = "2014 Anne and Grant"


# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("127847390583") is False
    assert checksum("123456789012") is True



def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
    with pytest.raises(TypeError):
        checksum(786936224306)
    with pytest.raises(TypeError):
        checksum(1)
    with pytest.raises(TypeError):
        checksum(-1)
    with pytest.raises(TypeError):
        checksum(-3.2)

    with pytest.raises(ValueError):
        checksum("1")
    with pytest.raises(ValueError):
        checksum("1234567890")
    with pytest.raises(ValueError):
        checksum("43783920192837483")
