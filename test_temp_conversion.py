# test the various temperature conversions

import numpy.testing as npt
from nose.tools import raises

from temp_conversion import fahr_to_kelvin
from temp_conversion import fahr_to_celsius

def test_basic():
	"""basic test"""
	npt.assert_almost_equal(fahr_to_kelvin(20), 266.483333, decimal=2)

def test_zero_kelvin():
	"""test for zero kelvin"""
	npt.assert_almost_equal(fahr_to_kelvin(-459.67), 0.0, decimal=2)

@raises(TypeError)
def test_temp_string():
	"""check that a type error occurs"""
	assert fahr_to_kelvin("SomeTemperature")
