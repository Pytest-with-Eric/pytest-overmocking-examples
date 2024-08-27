from unittest.mock import patch
from src.payment_processor import PaymentProcessor


@patch("requests.post")  # Incorrect patch target
def test_process_payment(mock_post):
    mock_post.return_value.json.return_value = {"status": "success"}
    processor = PaymentProcessor("https://fakegateway.com")
    result = processor.process_payment(100)

    assert result is True
    mock_post.assert_called_once_with(
        "https://fakegateway.com/pay", json={"amount": 100}
    )
