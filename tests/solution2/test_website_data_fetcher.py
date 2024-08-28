from unittest.mock import patch
from src.website_data_fetcher import WebsiteDataFetcher


class FakeDatabaseAdapter:
    def __init__(self):
        self.data_store = []

    def store_data(self, data):
        self.data_store.append(data)


@patch.object(WebsiteDataFetcher, "fetch_data_from_api")
def test_fetch_and_store(mock_fetch_data_from_api):
    # Setup the fake response from the API
    mock_fetch_data_from_api.return_value = {"name": "Example", "value": 123}

    # Use the fake database adapter
    fake_db_adapter = FakeDatabaseAdapter()
    fetcher = WebsiteDataFetcher(fake_db_adapter)

    # Act: Fetch and store the data
    result = fetcher.fetch_and_store("https://api.example.com/data")

    # Assert: Check that the data was stored correctly
    assert result is True
    assert fake_db_adapter.data_store == [{"name": "Example", "value": 123}]
