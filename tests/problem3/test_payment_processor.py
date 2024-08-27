from unittest.mock import Mock


class PaymentProcessor:
    def process_payment(self, amount, currency="USD"):
        # Imagine this sends a payment request
        return True


def test_process_payment():
    mock_processor = Mock(PaymentProcessor)
    mock_processor.process_payment.return_value = True

    # Notice that we're calling the method with an extra argument not in the real method
    result = mock_processor.process_payment(100, "USD", "EXTRA_ARG")

    assert result is True
