from lib.tyre import Tyre
from unittest import mock
from datetime import datetime, date


"""
Initialises correctly
"""
def test_initialises_correctly():
    tyre = Tyre()
    assert isinstance(tyre, Tyre)
    assert tyre.readings == []

@mock.patch('date.today')
def test_takes_reading_with_timestamp_and_appends_to_start_of_readings_list():
	date.today.return_value = date(2020, 1, 1)
	tyre = Tyre()
	tyre.take_reading(33, 2)
	# print(datetime.date.today())
	assert tyre.readings[0] == {"timestamp": date(2020, 1, 1), "pressure": 33, "tread_depth": 2}
      