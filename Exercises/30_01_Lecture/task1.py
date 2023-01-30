from datetime import datetime
from unittest.mock import patch


@patch("datetime.datetime")
def test_detetime_now(self, mock_datetime):
    mock_datetime.now = lambda: datetime(2023, 1, 29, 10, 0, 0)
    print(mock_datetime.now())

test_detetime_now(datetime)