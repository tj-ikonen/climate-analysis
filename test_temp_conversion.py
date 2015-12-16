import temp_conversion

def test_temperature():
    assert round(temp_conversion.fahr_to_kelvin(20), 6) == 266.483333