import requests


class WebsiteDataFetcher:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def fetch_data_from_api(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None

    def fetch_and_store(self, url):
        data = self.fetch_data_from_api(url)
        if data:
            self.db_adapter.store_data(data)
            return True
        return False


class RealDatabaseAdapter:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def store_data(self, data):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO api_data (name, value) VALUES (?, ?)",
            (data["name"], data["value"]),
        )
        self.db_connection.commit()
