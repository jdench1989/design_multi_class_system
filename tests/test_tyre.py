from lib.tyre import Tyre
from datetime import datetime
from unittest.mock import patch


"""
Initialises correctly
"""
def test_initialises_correctly():
    tyre = Tyre()
    assert isinstance(tyre, Tyre)
    assert tyre.readings == []

# patch overrides datetime class functionality specifically in the module given "lib.tyre.datetime" for this test
@patch('lib.tyre.datetime')
# patch creates a mock object which is passed in as a parameter to the test function
def test_takes_reading_with_timestamp_and_appends_to_start_of_readings_list(mock_datetime): 
    # mock object is then accessible within the function to be able to mock the return value
	mock_datetime.datetime.today.return_value = datetime(2020, 1, 1)
	tyre = Tyre()
	tyre.take_reading(33, 2)
	assert tyre.readings[0] == {"timestamp": datetime(2020, 1, 1), "pressure": 33, "tread_depth": 2}