#!/usr/bin/env python3

""" Module to test exercise1.py """

__author__ = 'Anne Simon', 'Grant Wheeler'
__email__ = "anne.simon@mail.utoronto.ca", "grant.wheeler@mail.utoronto.ca"
__copyright__ = "2014 Anne and Grant"

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1

#inputs that output TypeError and ValueError

    with pytest.raises(TypeError):
        decide_rps(3, 4)
    with pytest.raises(ValueError):
        decide_rps("rock", "Paper")
    with pytest.raises(ValueError):
        decide_rps("scissors", "paper")
    with pytest.raises(TypeError):
        decide_rps(3, "Paper")
    with pytest.raises(TypeError):
        decide_rps("PAPER", "paper")