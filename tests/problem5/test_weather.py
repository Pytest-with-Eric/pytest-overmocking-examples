from unittest.mock import Mock


class WeatherData:
    def get_temperature(self):
        # Imagine this method returns the temperature
        return 72

    def get_humidity(self):
        # Imagine this method returns the humidity
        return 55


class WeatherClient:
    def fetch_weather(self, location):
        # Imagine this method fetches weather data from an external API
        return WeatherData()


class WeatherService:
    def __init__(self, client):
        self.client = client

    def get_weather_report(self, location):
        weather_data = self.client.fetch_weather(location)
        temperature = weather_data.get_temperature()
        humidity = weather_data.get_humidity()
        return f"The temperature is {temperature}°F and the humidity is {humidity}%."


def test_get_weather_report():
    mock_client = Mock()
    mock_weather_data = Mock()

    # Set the return values for the methods of the WeatherData mock
    mock_weather_data.get_temperature.return_value = 72
    mock_weather_data.get_humidity.return_value = 55

    # Set the return value for the fetch_weather method of the mock client
    mock_client.fetch_weather.return_value = mock_weather_data

    service = WeatherService(mock_client)

    report = service.get_weather_report("New York")

    assert report == "The temperature is 72°F and the humidity is 55%."
    mock_client.fetch_weather.assert_called_once_with("New York")
    mock_weather_data.get_temperature.assert_called_once()
    mock_weather_data.get_humidity.assert_called_once()
