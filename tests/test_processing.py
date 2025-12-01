from unittest import result

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_data):
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(sample_data):
    result = filter_by_state(sample_data, "CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data, reverse=True)
    dates = [item["date"] for item in result]
    assert dates == [
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572",
    ]


def test_sort_by_date_ascending(sample_data):
    result
